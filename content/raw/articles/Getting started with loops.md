언제부터 'AI한테 시킨다'가 아니라 '루프를 짠다'가 됐을까요.

Claude Code 팀이 이번 주에 루프를 공식 분류하면서, 매 단계 내가 사람으로서 내려놓는 판단이 뭔지를 드러냈습니다. 확인부터 지시까지요.

잘 오르면 자동화, 잘못 오르면 나 몰래 틀리는 사다리입니다. 그 갈림길을 정리했습니다 🧵

[](https://www.threads.com/@choi.openai)

[choi.openai](https://www.threads.com/@choi.openai)

[1일](https://www.threads.com/@choi.openai/post/DadwxnsE0Dq)

·작성자

1/ 원래는 이랬습니다. 프롬프트를 하나 치면 Claude가 코드를 읽고, 고치고, 테스트를 돌려 결과를 건네줍니다. 그러면 내가 확인하고 다음 프롬프트를 칩니다. 매 턴을 사람이 끊는 구조죠.

루프는 여기서 사람을 뺍니다. Claude Code 팀은 루프를 '멈춤 조건에 닿을 때까지 에이전트가 같은 사이클을 반복하는 것'이라고 정의했습니다. 무엇이 시작시키고 무엇이 멈추게 하느냐, 어떤 기능을 쓰느냐, 어떤 일에 맞느냐로 네 종류로 나눠 놓았고요.

그동안 커뮤니티가 '루프 엔지니어링'이라 부르며 각자 정의하던 걸, 만든 팀이 이번 주에 한 장으로 정리해 냈습니다. 이 글은 그 네 칸을 아래에서 위로 하나씩 짚습니다.

[](https://www.threads.com/@choi.openai)

[choi.openai](https://www.threads.com/@choi.openai)

[1일](https://www.threads.com/@choi.openai/post/Dadwy5ME7zd)

·작성자

2/ 맨 아래 칸은 턴 기반 루프입니다. 사실 프롬프트 하나가 이미 작은 루프입니다.

Claude가 맥락을 모으고, 행동하고, 자기 점검을 하고, 필요하면 다시 돌고 나서 답합니다. 시작은 내 프롬프트, 멈춤은 Claude가 '됐다'고 판단하는 순간이죠.

여기서 내가 손에서 놓는 건 '확인'의 일부입니다. 매번 내 눈으로 하던 점검을 SKILL.md에 규칙으로 적어두면, Claude가 그만큼 스스로 검사하고 넘어옵니다. 점검이 정량적일수록, 그러니까 눈금으로 잴 수 있는 것일수록 Claude가 통과 여부를 스스로 판정하기 쉽습니다.

예를 들어 화면을 고쳤으면 편집이 됐다는 걸로 끝내지 말고, 브라우저를 띄워 직접 눌러보고 상태 변화와 콘솔 오류까지 확인하게 시키는 겁니다. 그래야 왕복하는 턴 수가 줄어듭니다.

[](https://www.threads.com/@choi.openai)

[choi.openai](https://www.threads.com/@choi.openai)

[1일](https://www.threads.com/@choi.openai/post/Dadwzf_E84M)

·작성자

3/ 그다음 칸은 목표 기반 루프, /goal입니다. 한 턴으로 안 될 때 씁니다.

문제는 Claude가 언제 멈출지 스스로 정하게 두면 '이만하면 됐다'며 일찍 손을 뗀다는 데 있습니다. 그래서 done이 뭔지를 내가 못 박아두면, Claude가 멈추려 할 때마다 평가 모델이 그 조건을 확인하고, 미달이면 다시 일을 시킵니다. 목표를 이룰 때까지, 또는 내가 정한 시도 횟수에 닿을 때까지요.

여기서 내려놓는 건 '멈춤 조건'입니다. 테스트 몇 개 통과나 점수 몇 점처럼 딱 떨어지는 기준일수록 잘 작동합니다. 예를 들어 '홈페이지 라이트하우스 점수를 90 이상으로 올리고, 다섯 번 시도한 뒤 멈춰'처럼 목표와 상한을 같이 걸어둡니다.

[](https://www.threads.com/@choi.openai)

[choi.openai](https://www.threads.com/@choi.openai)

[1일](https://www.threads.com/@choi.openai/post/Dadw0Xck98o)

·작성자

4/ 그 위 칸은 시간 기반 루프, /loop과 /schedule입니다. 일이 정해진 간격으로 돌아올 때 씁니다.

매일 아침 Slack 메시지를 요약하는 것처럼 하는 일은 그대로고 입력만 바뀌는 경우가 여기 맞습니다. 내 PR이 리뷰를 받거나 CI가 깨지는지처럼 바깥 시스템을 주기적으로 들여다보고 달라진 것에 반응하는 일도 마찬가지고요.

내려놓는 건 '시작 트리거'입니다. 언제 돌릴지를 내가 매번 누르지 않는 거죠. /loop은 내 컴퓨터에서 도니까 끄면 멈추고, 클라우드에 올려 계속 돌리려면 /schedule로 루틴을 만듭니다. 멈춤은 내가 취소하거나, PR이 병합되고 큐가 비는 것처럼 일이 끝나는 순간입니다.

[](https://www.threads.com/@choi.openai)

[choi.openai](https://www.threads.com/@choi.openai)

[1일](https://www.threads.com/@choi.openai/post/Dadw07Qk_FE)

5/ 맨 위 칸은 프로액티브 루프입니다. 이벤트나 스케줄로 돌고, 그 순간 사람은 실시간으로 붙어 있지 않습니다. 버그 리포트 처리나 이슈 분류처럼 잘 정의된 일이 계속 흘러들어올 때 쓰는 자리죠.

여기서 내려놓는 건 '지시 자체'입니다. /schedule로 깨우고, /goal로 끝을 정하고, 동적 워크플로우로 일을 여러 서브에이전트에 뿌리고, 오토 모드로 매번 권한을 묻지 않게 묶습니다. 앞의 세 칸을 다 합친 다음, 프롬프트를 던지는 사람마저 뺀 단계입니다.

동적 워크플로우는 제가 6월에 한 번 다뤘는데, 하나의 작업을 최대 1,000개 서브에이전트로 쪼개 그중 최대 16개를 동시에 돌리는 기능입니다. 지금은 리서치 프리뷰로 열려 있습니다.

[](https://www.threads.com/@choi.openai)

[choi.openai](https://www.threads.com/@choi.openai)

[2026-06-03](https://www.threads.com/@choi.openai/post/DZHHjRwj7Mm)


---
https://claude.com/blog/getting-started-with-loops
Learn how the Claude Code team defines agentic loops, with practical guidance on progressing from turn-based to goal-based, time-based, and proactive loops—and when to use each.

- Category
    
    [Claude Code](https://claude.com/blog/category/claude-code)
    
- Product
    
    Claude Code
    
- Date
    
    June 30, 2026
    
- Reading time
    
    5
    
    min
    
- Share
    
    [Copy link](https://claude.com/blog/getting-started-with-loops#)
    

There’s a lot of talk right now about "designing loops" instead of prompting your coding agent. If you spend some time on X trying to pin down what a loop actually is, you'll come across multiple different answers. 

On the Claude Code team, we define **loops as agents repeating cycles of work until a stop condition is met**. We categorize a few different types of loops based on:

- How they are triggered
- How they are stopped
- What Claude Code primitive is used
- What type of task is most appropriate for each.

We’ll cover the main loop types, when to use each, and how to maintain code quality while managing token usage. Not all tasks require complex loops; start with the simplest solution and use these patterns selectively. 

- [
    
    ](https://claude.com/download)
- [
    
    ](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code)
- [
    
    ](https://plugins.jetbrains.com/plugin/27310-claude-code-beta-)
- [
    
    ](https://claude.ai/redirect/claudedotcom.v1.e02a5a8f-7058-4f48-8e44-8b549166c6cf/code)
- [
    
    ](https://slack.com/oauth/v2/authorize?client_id=1601185624273.8899143856786&scope=app_mentions:read,assistant:write,channels:history,channels:read,chat:write,files:read,files:write,groups:history,groups:read,im:history,im:read,im:write,mpim:history,reactions:write,users:read,users:read.email,commands,search:read.public&user_scope=bookmarks:read,channels:history,channels:read,chat:write,emoji:read,files:read,groups:history,groups:read,groups:write,im:history,im:read,im:write,links:read,mpim:history,mpim:read,mpim:write,mpim:write.topic,pins:read,reactions:read,reactions:write,remote_files:read,team:read,users:read,users:read.email,search:read.public,search:read.private,search:read.im,search:read.mpim,search:read.files,search:read.users,canvases:read,canvases:write)

irm https://claude.ai/install.ps1 | iex

Copy command to clipboard

Or read the [documentation](https://code.claude.com/docs/en/overview)

## **Turn-based loops**

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a43eb603762e725a739d98c_8ace2295.png)

- **Triggered by**: A user prompt.
- **Stop criteria**: Claude judges it has completed the task or needs additional context.
- **Best used for:** Shorter tasks that are not part of a regular process or schedule.
- **Managed usage by:** Write specific prompts and improve verification using skills to reduce the number of turns.**‍**

Every prompt you send starts a manual loop with you directing each turn. Claude gathers context, takes action, checks its work, repeats if needed, and responds. We call this the agentic loop.

For example, ask Claude to create a like button. It reads your code, makes the edit, runs the tests, and hands back something it _believes_ works. You then manually check the work, and write the next prompt.

You can improve the verification step by encoding your manual steps as a SKILL.md so Claude can check more of its own work, end-to-end. This should include tools or connectors to allow Claude to _see_, _measure_ or _interact_ with the result. The more quantitative the checks are, the easier it is for Claude to self-verify. 

For example, in your SKILL.md file you may specify:

```plaintext
--- 
name: verify-frontend-change 
description: Verify any UI change end-to-end before declaring it done. 
--- 

# Verifying frontend changes 
Never report a UI change as complete based on a successful edit alone. Verify it the way a human reviewer would: 

1. Start the dev server and open the edited page in the browser. 

2. Interact with the change directly. For a new control (button, input, toggle): click it, confirm the expected state change, and screenshot before/after. 

3. Check the browser console: zero new errors or warnings. 

4. Use the Chrome Devtools MCP, run a performance trace and audit Core Web Vitals.

If any step fails, fix the issue and rerun from step 1 — do not hand back partially verified work.
```

## **Goal-based loop (/goal)**

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a43eb603762e725a739d98f_c6fa9ae5.png)

- **Triggered by**: A manual prompt in real-time.
- **Stop criteria**: Goal achieved OR maximum number of turns reached.
- **Best used for:** Tasks that have verifiable exit criteria.
- **Managed usage by:** Setting a specific completion criteria and explicit turn caps, “stop after 5 tries.”

Sometimes, a single turn is not enough, especially for more complex tasks. Agents do better when they can iterate. You can extend how long Claude keeps iterating by defining what done looks like with /goal.

When you define the success criteria, Claude doesn’t have to make a determination on what is “good enough” and end the loop early. Each time Claude tries to stop, an evaluator model checks your condition and sends it back to work until the goal is met or a number of turns you define is reached.

This is why deterministic criteria, such as number of tests passed or clearing a certain score threshold, are so effective.

For example:

```plaintext
/goal get the homepage Lighthouse score to 90 or above, stop after 5 tries.
```

## **Time-based loop (/loop and /schedule)**

- **Triggered by**: A specified time interval.
- **Stop criteria**: You cancel it, or the work completes (the PR merges, the queue is empty). 
- **Best used for:** For recurring work, or interfacing with external environments / systems. 
- **Managed usage by:** Set longer intervals or react based on events rather than time.

Some agentic work is recurring: the task stays the same and only the inputs change. For example, summarizing Slack messages every morning. Other work depends on external systems, and a simple way to interface with one is to check it on an interval and react to what changed. For example, a PR which may receive code reviews or fail CI.

For these, you can trigger when Claude runs with `/loop` which re-runs a prompt on an interval. For example:

```plaintext
/loop 5m check my PR, address review comments, and fix failing CI
```

`/loop` runs on your computer, so if you turn it off, it stops. You can move the loop to the cloud by creating a routine with  `/schedule`. 

## **Proactive loops**

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a43eb603762e725a739d989_eb9e496a.png)

- **Triggered by**: An event or schedule, with no human in real time. 
- **Stop criteria**: Each task exits when its goal is met. The routine itself runs until you turn it off. 
- **Best used for:** Recurring streams of well-defined work: bug reports, issue triage, migrations, dependency upgrades, etc.
- **Managed usage by:** Routing routines to smaller, faster models and using the most capable model for judgment calls. 

The primitives above, along with other Claude Code features like **auto mode** and **dynamic workflows** (research preview) can be composed into a loop for long-running work. 

For example, to handle incoming feedback, you can use:

1. **`/schedule`** (research preview) to run a routine that checks for new reports
2. **`/goal`** to define what done looks and **skills** to document how to verify it
3. **Dynamic workflows** to orchestrate agents that triage each report, fix it, and review the fix
4. **Auto mode** so the routine runs without stopping to ask for permission

Putting it together, a prompt could look like this:

```plaintext
/schedule every hour: check #project-feedback for bug reports. /goal: don't stop until every report found this run is triaged, actioned, and responded to. When fixing a bug, use a workflow to explore three solutions in parallel worktrees and have a judge adversarially review them.
```

## **Maintaining code quality**

The quality of a loop’s output depends on the system around it. When designing the system:

- **Keep the codebase itself clean**: Claude follows patterns and conventions that already exist in your codebase.
- **Give Claude a way to verify its own work**: Encode what good looks like for you and your team with [skills](https://code.claude.com/docs/en/skills).
- **Make docs easy to reach:** Frameworks and libraries docs have up-to-date best practices.
- **Use a second agent for code reviews**: A reviewer with fresh context is less biased and not influenced by the main agent’s reasoning. You can use the built-in `/code-review` skill or [Code Review](https://code.claude.com/docs/en/code-review) for Github.

When an individual result doesn’t meet the standard, don’t stop at fixing the individual issue, try to encode it to improve the system for all future iterations.

## **Managing token usage**

To manage token usage, loops should have clear boundaries: 

- **Choose the right primitive and model for the job:** Smaller tasks don’t need multiple agents or loops. Some tasks can use cheaper and faster models. 
- **Define clear success and stop criteria:** Be specific about what done looks like so Claude can arrive at the solution sooner (but not too soon). 
- **Pilot before a large run:** Dynamic workflows can spawn hundreds of agents. Gauge usage on a smaller slice of the work first.
- **Use scripts for deterministic work**: Running a script is cheaper than reasoning through the steps. For example, a PDF skill can ship a form-filling script that Claude runs each time, instead of re-deriving the code.
- **Don’t run routines more often that you need to:** Match the interval to how often the thing you’re watching changes
- **Review usage:** The `/usage` command breaks down recent usage by skills, subagents, and MCPs, `/goal` with no arguments shows number of turns and token usage so far, `/workflows` shows each agent’s token usage and you can stop an agent at any time.

## **Getting started**

To summarize: 

|Loop|You hand off|Use it when|Reach for|
|---|---|---|---|
|Turn-based|The check|You're exploring or deciding|Custom verification skills|
|Goal-based|The stop condition|You know what done looks like|`/goal`|
|Time-based|The trigger|The work happens outside your project on a schedule|`/loop`, `/schedule`|
|Proactive|The prompt|The work is recurring and well-defined|All of the above, and dynamic workflows|

To get started with loops, look at the work you already do. Pick one task where you’re the bottleneck and ask which piece you could hand off: can you write the verification check? Is the goal clear enough? Does the work arrive on a schedule?

Once you have an idea, run the loop, observe the results like where it stalls or over-reaches, and don’t be afraid to iterate on it.

For more information, read the Claude Code docs on [running agents in parallel,](https://code.claude.com/docs/en/agents) as well as the [loop](https://code.claude.com/docs/en/goal), [schedule](https://code.claude.com/docs/en/routines), [goal](https://code.claude.com/docs/en/goal), and [dynamic workflows](https://code.claude.com/docs/en/workflows#orchestrate-subagents-at-scale-with-dynamic-workflows) pages. 

_This article was written by Delba de Oliveira and Michael Segner_