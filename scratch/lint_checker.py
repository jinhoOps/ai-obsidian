import os
import re
import json

wiki_root = "content/wiki"
valid_types = {"entity", "concept", "comparison", "source", "synthesis", "meta"}
required_fields = {"title", "type", "tags", "sources", "created", "updated", "draft"}

# Manual simple YAML parser to avoid external dependencies
def parse_frontmatter_manual(text):
    meta = {}
    lines = text.strip().split('\n')
    current_key = None
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if line.startswith('-'):
            if current_key:
                val = line[1:].strip().strip('"').strip("'")
                if current_key not in meta or not isinstance(meta[current_key], list):
                    meta[current_key] = []
                meta[current_key].append(val)
            continue
        if ':' in line:
            parts = line.split(':', 1)
            key = parts[0].strip()
            val = parts[1].strip()
            current_key = key
            if val.startswith('[') and val.endswith(']'):
                items = [i.strip().strip('"').strip("'") for i in val[1:-1].split(',')]
                meta[key] = [i for i in items if i]
            elif val.startswith('"') and val.endswith('"'):
                meta[key] = val[1:-1]
            elif val.startswith("'") and val.endswith("'"):
                meta[key] = val[1:-1]
            elif val.lower() == 'false':
                meta[key] = False
            elif val.lower() == 'true':
                meta[key] = True
            else:
                meta[key] = val
    return meta

# 1. Collect all valid wiki markdown files and their slugs
wiki_files = {}  # slug -> absolute path
slug_to_meta = {}  # slug -> frontmatter dict

for root, dirs, files in os.walk(wiki_root):
    for f in files:
        if f.endswith(".md"):
            path = os.path.join(root, f)
            slug = os.path.splitext(f)[0].lower()
            wiki_files[slug] = path

# Function to parse markdown frontmatter
def parse_markdown(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()
    
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if not match:
        return None, content
    
    try:
        meta = parse_frontmatter_manual(match.group(1))
        return meta, content[match.end():]
    except Exception as e:
        return {"error": str(e)}, content

# Load metadata and check frontmatter errors
frontmatter_errors = []
link_patterns = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]")

all_links = {} # source_slug -> set of target_slugs
referenced_slugs = set()

for slug, path in wiki_files.items():
    meta, body = parse_markdown(path)
    if not meta:
        frontmatter_errors.append((path, "No frontmatter found"))
        continue
    if "error" in meta:
        frontmatter_errors.append((path, f"YAML parse error: {meta['error']}"))
        continue
    
    # Check required fields
    missing = required_fields - set(meta.keys())
    if missing:
        frontmatter_errors.append((path, f"Missing fields: {list(missing)}"))
    
    # Check invalid draft
    if "draft" in meta and meta["draft"] is not False:
        if meta["draft"] is True:
            frontmatter_errors.append((path, "draft is True"))
            
    slug_to_meta[slug] = meta
    
    # Extract links in body
    links = link_patterns.findall(body)
    target_slugs = set()
    for l in links:
        # clean link (obsidian format can have subdirectories like wiki/ai/Harness_Engineering)
        clean_target = os.path.splitext(os.path.basename(l))[0].strip().lower().replace(" ", "-")
        target_slugs.add(clean_target)
        referenced_slugs.add(clean_target)
    all_links[slug] = target_slugs

# 2. Check Broken Links & Orphan Pages & Ghost Concepts
broken_links = {} # source_slug -> set of broken target_slugs
ghost_concepts = set()

for src, targets in all_links.items():
    for tgt in targets:
        if tgt not in wiki_files:
            if tgt == "" or tgt.startswith("http"):
                continue
            if src not in broken_links:
                broken_links[src] = set()
            broken_links[src].add(tgt)
            ghost_concepts.add(tgt)

# Orphan pages: pages that are not index/log and are not target of any link in the wiki
all_targets = set()
for targets in all_links.values():
    all_targets.update(targets)

# Index/portal pages are not orphans
ignored_orphans = {"index", "log", "wiki-log", "wiki-index"}
orphan_pages = []
for slug, path in wiki_files.items():
    if slug not in all_targets and slug not in ignored_orphans:
        orphan_pages.append((slug, path))

# 3. Check Index inconsistencies
index_path = os.path.join(wiki_root, "index.md")
index_meta, index_body = parse_markdown(index_path)

# Extract all links in index.md
index_links = set()
if index_body:
    links = link_patterns.findall(index_body)
    for l in links:
        clean_target = os.path.splitext(os.path.basename(l))[0].strip().lower().replace(" ", "-")
        index_links.add(clean_target)

# Compare index links to actual wiki files (excluding index.md and log.md itself)
actual_slugs = set(wiki_files.keys()) - {"index", "log"}
missing_in_index = actual_slugs - index_links
extra_in_index = index_links - actual_slugs

# Count check
total_pages_actual = len(actual_slugs)
total_sources_actual = len([s for s in actual_slugs if slug_to_meta.get(s, {}).get("type") == "source"])

# Parse stats in index.md
stats_errors = []
if index_body:
    page_match = re.search(r"-\s+\*\*총\s+페이지\s+수\*\*:\s*(\d+)", index_body)
    source_match = re.search(r"-\s+\*\*총\s+ingest된\s+소스\s+수\*\*:\s*(\d+)", index_body)
    
    if page_match:
        reported_pages = int(page_match.group(1))
        if reported_pages != total_pages_actual:
            stats_errors.append(f"Page count mismatch: index.md says {reported_pages}, actual is {total_pages_actual}")
    else:
        stats_errors.append("Page count stat not found in index.md")
        
    if source_match:
        reported_sources = int(source_match.group(1))
        if reported_sources != total_sources_actual:
            stats_errors.append(f"Source count mismatch: index.md says {reported_sources}, actual is {total_sources_actual}")
    else:
        stats_errors.append("Source count stat not found in index.md")

# Output diagnostics JSON
diagnostics = {
    "total_pages": len(wiki_files),
    "frontmatter_errors": [(os.path.basename(p), err) for p, err in frontmatter_errors],
    "broken_links": {os.path.basename(wiki_files[src]): list(tgts) for src, tgts in broken_links.items()},
    "orphan_pages": [os.path.basename(p) for s, p in orphan_pages],
    "ghost_concepts": list(ghost_concepts),
    "index_missing": list(missing_in_index),
    "index_extra": list(extra_in_index),
    "stats_errors": stats_errors,
    "actual_counts": {
        "pages": total_pages_actual,
        "sources": total_sources_actual
    }
}

print(json.dumps(diagnostics, indent=2, ensure_ascii=False))
