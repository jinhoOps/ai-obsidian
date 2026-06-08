
# 0. 확인
https://github.com/garrytan/gstack#quick-start
## Quick start
1. Install gstack (30 seconds — see below)
2. Run `/office-hours` — describe what you're building
3. Run `/plan-ceo-review` on any feature idea
4. Run `/review` on any branch with changes
5. Run `/qa` on your staging URL
6. Stop there. You'll know if this is for you.

**Requirements:** [Claude Code](https://docs.anthropic.com/en/docs/claude-code), [Git](https://git-scm.com/), [Bun](https://bun.sh/) v1.0+, [Node.js](https://nodejs.org/) (Windows only)
-> 여기서 클로드 코드 대신 `Antigravity CLI` 기준으로 함 (이하 agy)
# 1. 설치
## step 1. 내 콤퓨타에 설치
claude 한테 agy 용으로 바꿔달라고함.

```
Install gstack for agy (Antigravity CLI):

1. Run this command:
   git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.gemini/antigravity/skills/gstack && cd ~/.gemini/antigravity/skills/gstack && ./setup

2. Add a "gstack" section to AGENTS.md (or GEMINI.md) with the following content:

## gstack

- For all web browsing, use the /browse skill from gstack. Never use built-in browser tools (mcp__antigravity-browser__* or similar).

### Available skills
/office-hours, /plan-ceo-review, /plan-eng-review, /plan-design-review, /design-consultation, /design-shotgun, /design-html, /review, /ship, /land-and-deploy, /canary, /benchmark, /browse, /connect-chrome, /qa, /qa-only, /design-review, /setup-browser-cookies, /setup-deploy, /setup-gbrain, /retro, /investigate, /document-release, /document-generate, /codex, /cso, /autoplan, /plan-devex-review, /devex-review, /careful, /freeze, /guard, /unfreeze, /gstack-upgrade, /learn

3. After completing the above, ask the user: "Do you also want to add gstack to the current project so teammates get it? If yes, I'll clone it into .agents/skills/gstack and add the gstack section to the project-level AGENTS.md."
```


## step 2. 팀 모드 - 공유 저장소 자동 업데이트(추천)

```
Set up gstack team mode for agy (Antigravity CLI):

1. Run this command from inside your repo:
   (cd ~/.gemini/antigravity/skills/gstack && ./setup --team) && ~/.gemini/antigravity/skills/gstack/bin/gstack-team-init required && git add .agents/ AGENTS.md && git commit -m "require gstack for AI-assisted work"

This switches to team mode, bootstraps the repo so teammates get gstack automatically, and commits the change.
Every agy session starts with a fast auto-update check (throttled to once/hour, network-failure-safe, completely silent).

Swap "required" for "optional" if you'd rather nudge teammates than block them.
```

## OpenClaw (agy 버전)
```
Set up gstack for OpenClaw (agy variant):

OpenClaw spawns agy sessions via ACP, so every gstack skill just works when agy has gstack installed. Paste this to your OpenClaw agent:

Install gstack: run git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.gemini/antigravity/skills/gstack && cd ~/.gemini/antigravity/skills/gstack && ./setup to install gstack for agy (Antigravity CLI). Then add a "Coding Tasks" section to AGENTS.md that says: when spawning agy sessions for coding work, tell the session to use gstack skills. Include these examples — security audit: "Load gstack. Run /cso", code review: "Load gstack. Run /review", QA test a URL: "Load gstack. Run /qa https://...", build a feature end-to-end: "Load gstack. Run /autoplan, implement the plan, then run /ship", plan before building: "Load gstack. Run /office-hours then /autoplan. Save the plan, don't implement."
```

## 2. 동작 확인
해야되나?
```
You:    I want to build a daily briefing app for my calendar.
You:    /office-hours
Claude: [asks about the pain — specific examples, not hypotheticals]

You:    Multiple Google calendars, events with stale info, wrong locations.
        Prep takes forever and the results aren't good enough...

Claude: I'm going to push back on the framing. You said "daily briefing
        app." But what you actually described is a personal chief of
        staff AI.
        [extracts 5 capabilities you didn't realize you were describing]
        [challenges 4 premises — you agree, disagree, or adjust]
        [generates 3 implementation approaches with effort estimates]
        RECOMMENDATION: Ship the narrowest wedge tomorrow, learn from
        real usage. The full vision is a 3-month project — start with
        the daily briefing that actually works.
        [writes design doc → feeds into downstream skills automatically]

You:    /plan-ceo-review
        [reads the design doc, challenges scope, runs 10-section review]

You:    /plan-eng-review
        [ASCII diagrams for data flow, state machines, error paths]
        [test matrix, failure modes, security concerns]

You:    Approve plan. Exit plan mode.
        [writes 2,400 lines across 11 files. ~8 minutes.]

You:    /review
        [AUTO-FIXED] 2 issues. [ASK] Race condition → you approve fix.

You:    /qa https://staging.myapp.com
        [opens real browser, clicks through flows, finds and fixes a bug]

You:    /ship
        Tests: 42 → 51 (+9 new). PR: github.com/you/app/pull/42
```

"매일 브리핑 앱"이라고 하셨죠 이 에이전트는 기능 요청이 아닌 고통을 들어줬기 때문에 "참모총장 AI를 구축하는 것"이라고 말했습니다. 여덟 가지 명령, 끝에서 끝까지. 그것은 부조종사가 아닙니다. 그것은 팀입니다.

## 스프린트

gstack은 도구 모음이 아니라 과정입니다. 기술은 스프린트가 진행되는 순서대로 진행됩니다:

**생각하기 → 계획 → 구축 → 검토 → 테스트 → 선박 → 반영**

각 기술은 다음 단계로 이어집니다. `/office-hours` 다음과 같은 디자인 문서를 작성합니다 `/plan-ceo-review` 읽는다. `/plan-eng-review` 다음과 같은 테스트 계획을 작성합니다 `/qa` 픽업. `/review` 다음과 같은 버그를 포착합니다 `/ship` 확인이 완료되었습니다. 모든 단계가 그 이전에 무엇이 있었는지 알기 때문에 균열을 통해 아무것도 떨어지지 않습니다.