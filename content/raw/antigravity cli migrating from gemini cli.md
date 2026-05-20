https://antigravity.google/docs/gcli-migration

Migrating from Gemini CLI
If you are an existing Gemini CLI user looking to migrate your workflow to Antigravity CLI, you have come to the right place. The guide below will help you get familiar with and up and running quickly in Antigravity CLI.

info
TL;DR: Antigravity CLI supports the majority of features from Gemini CLI. While there is not 100% feature parity, workflow defining features like Gemini CLI extensions (Antigravity plugins), Agent Skills, MCP servers, hooks, and subagents are all supported in Antigravity CLI.
On the first launch of Antigravity CLI, you should see Migration Options where you can choose to migrate your existing Gemini CLI extensions to the equivalent Antigravity Plugins.

info
Note: Some Gemini CLI extensions cannot be migrated 1:1 to Antigravity plugins as some components (e.g., custom themes) are not currently supported.
For the majority of users, you can now get started using Antigravity CLI with the workflows you have come to love in Gemini CLI. Antigravity CLI loads in the same context files and global Agent Skills as Gemini CLI does.

If you notice something not working the way it should or how you expect, refer to the specific details below.

Gemini CLI Extensions → Antigravity Plugins
Since Gemini CLI launched extensions (a way to extend the CLI by bundling and sharing capabilities), the industry has standardized on the term plugins. Antigravity plugins are supported in Antigravity CLI.

Users should be prompted on the first launch of Antigravity CLI to have their extensions automatically migrated to plugins. You can also run an explicit command from your terminal to migrate them:

bash
content_copy
agy plugin import gemini
Running the agy plugin import command will search for each locally installed extension and convert them to an Antigravity plugin:

text
content_copy
  [ok]    conductor
          - skills      : skipped (not found)
          - agents      : skipped (not found)
          ✔ commands    : 6 processed (converted to skills)
          - mcpServers  : skipped (not found)
          - hooks       : skipped (not found)
  [ok]    google-workspace
          ✔ skills      : 6 processed
          - agents      : skipped (not found)
          ✔ commands    : 4 processed (converted to skills)
          ✔ mcpServers  : 1 processed
          - hooks       : skipped (not found)
Context Files (Rules)
Antigravity CLI 지원 경로:

Workspace Context: `GEMINI.md`, `AGENTS.md` (루트)
Global Context: `~/.gemini/antigravity-cli/GEMINI.md`

Agent Skills
Antigravity CLI는 `.agents/skills` 폴더를 프로젝트별 스킬 저장소로 사용합니다.

Attribute | Gemini CLI | Antigravity CLI
--- | --- | ---
기본 명령어 | `gemini` | `agy`
설정 경로 | `~/.gemini/` | `~/.gemini/antigravity-cli/`
프로젝트 설정 | `.gemini/` | `.agents/`
마이그레이션 | (N/A) | `agy plugin import gemini`

MCP Servers
Antigravity CLI는 `mcp_config.json` 파일을 통해 MCP 서버를 관리합니다.

Attribute | Gemini CLI | Antigravity CLI
--- | --- | ---
설정 위치 | `~/.gemini/settings.json` | `~/.gemini/antigravity-cli/mcp_config.json`
프로젝트 설정 | `.gemini/settings.json` | `.agents/mcp_config.json`
관리 명령 | `/mcp` | `/mcp`
