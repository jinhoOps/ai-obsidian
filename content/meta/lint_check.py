import os
import re
from datetime import datetime

WIKI_DIR = r"D:\jhkSandBox\CODE_AI\ai-obsidian\content\wiki"
RAW_DIR = r"D:\jhkSandBox\CODE_AI\ai-obsidian\content\raw"

def get_all_wiki_files():
    files = {}
    for root, dirs, filenames in os.walk(WIKI_DIR):
        # Skip graphify-out if it exists inside wiki
        if "graphify-out" in root:
            continue
        for f in filenames:
            if f.endswith(".md"):
                full_path = os.path.join(root, f)
                rel_path = os.path.relpath(full_path, WIKI_DIR).replace("\\", "/")
                key = os.path.splitext(rel_path)[0] # e.g. "concepts/agentic-workflow" or "index"
                name_without_ext = os.path.splitext(f)[0]
                files[key] = {
                    "full_path": full_path,
                    "rel_path": rel_path,
                    "filename": f,
                    "name": name_without_ext,
                    "dir": os.path.relpath(root, WIKI_DIR).replace("\\", "/")
                }
    return files

def get_all_raw_files():
    files = []
    for root, dirs, filenames in os.walk(RAW_DIR):
        for f in filenames:
            if f.endswith(".md"):
                full_path = os.path.join(root, f)
                rel_path = os.path.relpath(full_path, RAW_DIR).replace("\\", "/")
                files.append({
                    "full_path": full_path,
                    "rel_path": rel_path,
                    "filename": f
                })
    return files

def parse_frontmatter(content):
    frontmatter_re = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
    match = frontmatter_re.match(content)
    if match:
        try:
            fm_text = match.group(1)
            fm = {}
            for line in fm_text.split("\n"):
                if not line.strip() or line.strip().startswith("#"):
                    continue
                if ":" in line:
                    k, v = line.split(":", 1)
                    k = k.strip()
                    v = v.strip()
                    # Strip quotes if present
                    if (v.startswith('"') and v.endswith('"')) or (v.startswith("'") and v.endswith("'")):
                        v = v[1:-1]
                    # Parse list like [a, b, c]
                    if v.startswith("[") and v.endswith("]"):
                        inner = v[1:-1].strip()
                        # If it's a single unquoted path starting with content/ or wiki/ and ending with .md, do not split by comma
                        if (inner.startswith("content/") or inner.startswith("wiki/")) and inner.endswith(".md"):
                            v = [inner]
                        else:
                            quoted_items = re.findall(r'"([^"]*)"|\'([^\']*)\'', inner)
                            if quoted_items:
                                v = [item[0] or item[1] for item in quoted_items]
                            else:
                                items = inner.split(",")
                                v = [i.strip().strip('"').strip("'") for i in items if i.strip()]
                    elif v.lower() == "true":
                        v = True
                    elif v.lower() == "false":
                        v = False
                    fm[k] = v
            return fm, content[match.end():]
        except Exception as e:
            return "PARSE_ERROR", content
    return None, content

def extract_links(content):
    # Remove code blocks and inline code backticks to avoid parsing links inside code
    content_clean = re.compile(r"```.*?```", re.DOTALL).sub("", content)
    content_clean = re.compile(r"`.*?`").sub("", content_clean)
    
    # Matches [[link]] or [[link|text]] or [[link#header]]
    link_re = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
    links = link_re.findall(content_clean)
    # Normalize links
    normalized = []
    for l in links:
        l_norm = l.strip().replace("\\", "/")
        # If it has a path, take the filename part
        if "/" in l_norm:
            l_norm = l_norm.split("/")[-1]
        normalized.append(os.path.splitext(l_norm)[0] if l_norm.endswith(".md") else l_norm)
    return normalized

def check_date_format(date_val):
    if not date_val:
        return False
    if isinstance(date_val, datetime):
        return True
    if isinstance(date_val, (int, float)):
        return False
    date_str = str(date_val).strip()
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def run_lint():
    wiki_files = get_all_wiki_files()
    raw_files = get_all_raw_files()
    
    # Pre-calculate unique file names (case-insensitive)
    # Map lowercase filename (no ext) to its rel_path key(s)
    wiki_names_map = {}
    for key, info in wiki_files.items():
        name_lc = info["name"].lower()
        if name_lc not in wiki_names_map:
            wiki_names_map[name_lc] = []
        wiki_names_map[name_lc].append(key)
        
    reports = {
        "broken_links": [],  # HIGH: [[link]] but no file
        "orphans": [],       # MEDIUM: exists but not linked by anyone (except index)
        "ghosts": [],        # MEDIUM: link exists in text but file does not
        "frontmatter_errors": [], # HIGH: missing fields, bad types, bad dates
        "index_mismatch": [], # HIGH: index vs actual files
        "stale_content": [],  # MEDIUM: source updated but wiki page not
        "knowledge_gaps": []  # LOW: raw files not ingested, missing synthesis/comparison
    }
    
    all_links = {}
    incoming_links = {k: set() for k in wiki_files.keys()}
    
    file_metadata = {}
    
    # 1. Scan and parse each wiki file
    for key, info in wiki_files.items():
        try:
            with open(info["full_path"], "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            reports["frontmatter_errors"].append({
                "file": info["rel_path"],
                "error": f"파일 읽기 실패: {str(e)}"
            })
            continue
            
        fm, body = parse_frontmatter(content)
        file_metadata[key] = {"info": info, "frontmatter": fm, "content": content}
        
        # Check Frontmatter
        if fm == "PARSE_ERROR":
            reports["frontmatter_errors"].append({
                "file": info["rel_path"],
                "error": "YAML 파싱 오류"
            })
            continue
        elif fm is None:
            reports["frontmatter_errors"].append({
                "file": info["rel_path"],
                "error": "Frontmatter가 없습니다."
            })
            continue
            
        # Check required fields
        required_fields = ["title", "type", "tags", "sources", "created", "updated", "draft"]
        missing = [field for field in required_fields if field not in fm]
        if missing:
            reports["frontmatter_errors"].append({
                "file": info["rel_path"],
                "error": f"필수 필드 누락: {', '.join(missing)}"
            })
            
        # Check date format
        if "created" in fm and not check_date_format(fm["created"]):
            reports["frontmatter_errors"].append({
                "file": info["rel_path"],
                "error": f"created 날짜 형식 오류: {fm['created']} (YYYY-MM-DD 필요)"
            })
        if "updated" in fm and not check_date_format(fm["updated"]):
            reports["frontmatter_errors"].append({
                "file": info["rel_path"],
                "error": f"updated 날짜 형식 오류: {fm['updated']} (YYYY-MM-DD 필요)"
            })
            
        # Check type
        valid_types = ["entity", "concept", "comparison", "source", "synthesis", "meta"]
        if "type" in fm and fm["type"] not in valid_types:
            reports["frontmatter_errors"].append({
                "file": info["rel_path"],
                "error": f"잘못된 type: {fm['type']} (valid: {valid_types})"
            })
            
        # Extract links
        extracted = extract_links(body)
        all_links[key] = extracted
        
        # Track incoming links
        for l in extracted:
            l_lc = l.lower()
            if l_lc in wiki_names_map:
                for target_key in wiki_names_map[l_lc]:
                    incoming_links[target_key].add(key)
            else:
                reports["broken_links"].append({
                    "file": info["rel_path"],
                    "target": l,
                    "error": f"깨진 링크: 존재하지 않는 페이지 [[{l}]]"
                })
                if l not in reports["ghosts"]:
                    reports["ghosts"].append(l)
                    
    # 2. Orphans check
    for key, incoming in incoming_links.items():
        if key in ["index", "ai-rules", "log"]:
            continue
        if not incoming:
            reports["orphans"].append({
                "file": wiki_files[key]["rel_path"],
                "error": "아무 데서도 링크되지 않은 고아 페이지입니다."
            })

    # 3. Index mismatch check
    index_meta = file_metadata.get("index")
    if index_meta:
        index_content = index_meta["content"]
        index_links = set(extract_links(index_content))
        
        actual_sources = {k for k, v in file_metadata.items() if v.get("frontmatter") and v["frontmatter"].get("type") == "source"}
        
        for key, info in wiki_files.items():
            if key in ["index", "ai-rules", "log"]:
                continue
            # Check if name is linked in index
            name_lc = info["name"].lower()
            if name_lc not in [il.lower() for il in index_links]:
                reports["index_mismatch"].append({
                    "file": info["rel_path"],
                    "error": f"이 페이지는 index.md에 링크되어 있지 않습니다."
                })
                
        for l in index_links:
            if l.lower() not in wiki_names_map:
                reports["index_mismatch"].append({
                    "file": "index.md",
                    "error": f"index.md에 있는 링크 [[{l}]]는 존재하지 않는 파일입니다."
                })
                
        stat_pages_match = re.search(r"-\s*\*\*총 페이지 수\*\*:\s*(\d+)", index_content)
        stat_sources_match = re.search(r"-\s*\*\*총 ingest된 소스 수\*\*:\s*(\d+)", index_content)
        
        total_wiki_pages = len([k for k in wiki_files.keys() if k not in ["index", "ai-rules", "log"]])
        total_wiki_sources = len(actual_sources)
        
        if stat_pages_match:
            stat_pages = int(stat_pages_match.group(1))
            if stat_pages != total_wiki_pages:
                reports["index_mismatch"].append({
                    "file": "index.md",
                    "error": f"통계 불일치: index.md에 명시된 총 페이지 수({stat_pages})와 실제 페이지 수({total_wiki_pages})가 다릅니다."
                })
        else:
            reports["index_mismatch"].append({
                "file": "index.md",
                "error": "통계 누락: '총 페이지 수' 통계가 존재하지 않습니다."
            })
            
        if stat_sources_match:
            stat_sources = int(stat_sources_match.group(1))
            if stat_sources != total_wiki_sources:
                reports["index_mismatch"].append({
                    "file": "index.md",
                    "error": f"통계 불일치: index.md에 명시된 총 소스 수({stat_sources})와 실제 소스 수({total_wiki_sources})가 다릅니다."
                })
        else:
            reports["index_mismatch"].append({
                "file": "index.md",
                "error": "통계 누락: '총 ingest된 소스 수' 통계가 존재하지 않습니다."
            })

    # 4. Stale Content check
    raw_mtimes = {}
    for rf in raw_files:
        try:
            mtime = os.path.getmtime(rf["full_path"])
            dt = datetime.fromtimestamp(mtime)
            raw_mtimes[rf["rel_path"]] = dt
            raw_mtimes[rf["filename"]] = dt
        except Exception:
            pass
            
    for key, meta in file_metadata.items():
        fm = meta.get("frontmatter")
        if not fm or "sources" not in fm:
            continue
        sources = fm["sources"]
        if not sources or not isinstance(sources, list):
            continue
        for src in sources:
            src_normalized = src.replace("content/raw/", "").replace("content\\raw\\", "")
            src_mtime = raw_mtimes.get(src_normalized) or raw_mtimes.get(os.path.basename(src_normalized))
            if src_mtime:
                wiki_updated = fm.get("updated")
                if wiki_updated:
                    if isinstance(wiki_updated, datetime):
                        wiki_updated_dt = wiki_updated
                    elif isinstance(wiki_updated, str):
                        try:
                            wiki_updated_dt = datetime.strptime(wiki_updated.strip(), "%Y-%m-%d")
                        except ValueError:
                            continue
                    else:
                        continue
                    
                    if (src_mtime.date() - wiki_updated_dt.date()).days > 1:
                        reports["stale_content"].append({
                            "file": meta["info"]["rel_path"],
                            "source": src,
                            "wiki_updated": wiki_updated_dt.strftime("%Y-%m-%d"),
                            "source_mtime": src_mtime.strftime("%Y-%m-%d"),
                            "error": f"낡은 내용: 소스 파일({src})이 {src_mtime.strftime('%Y-%m-%d')}에 변경되었으나, 위키 페이지는 {wiki_updated_dt.strftime('%Y-%m-%d')}에 업데이트되었습니다."
                        })

    # 5. Knowledge gaps check
    ingested_sources = set()
    for key, meta in file_metadata.items():
        fm = meta.get("frontmatter")
        if fm and "sources" in fm:
            sources = fm["sources"]
            if isinstance(sources, list):
                for src in sources:
                    src_normalized = src.replace("content/raw/", "").replace("content\\raw\\", "")
                    ingested_sources.add(src_normalized.lower())
                    ingested_sources.add(os.path.basename(src_normalized).lower())
                
    for rf in raw_files:
        rf_name = rf["filename"].lower()
        rf_rel = rf["rel_path"].lower()
        if rf_name in ["ai-rules.md", "index.md", "raw-layer-rules.md"]:
            continue
        if rf_name not in ingested_sources and rf_rel not in ingested_sources:
            reports["knowledge_gaps"].append({
                "file": rf["rel_path"],
                "error": "미인제스트 소스: raw 파일이 위키에 반영되어 있지 않습니다."
            })
            
    return reports

if __name__ == "__main__":
    import json
    res = run_lint()
    print(json.dumps(res, indent=2, ensure_ascii=False))
