# Objective 1: Parallel Tool Calls

[← Back to objectives index](README.md) · [Back to main index](../../README.md)

> **Exam objective:** Configure agentic loops to emit multiple tool calls within a single response turn, enabling parallel execution of independent subtasks and reducing total round-trip latency.

---

### Q1.
An architect is tuning an agent that must inspect five unrelated configuration files before recommending a deployment fix. Each file read takes about the same time, and the agent currently reads them one at a time in separate turns. Which redesign best aligns with the objective?

A. Keep sequential reads so the agent can narrate after each file
B. Emit five independent file-read tool calls in one response turn
C. Replace file reads with a single summary request to the user
D. Read only one file and infer the rest from naming conventions

**Answer:** B
**Explanation:** The files are independent, so issuing all five reads in one turn minimizes round-trip latency while preserving full evidence gathering. Sequential reads add unnecessary delay, and the other options reduce accuracy by skipping or guessing at needed inputs.

### Q2.
An agent must compare API error logs, database metrics, and queue depth snapshots to determine whether an outage is caused by backpressure or a schema issue. None of the three inputs depends on the others. What is the best tool-call pattern?

A. Query all three sources in parallel, then synthesize once results return
B. Query the logs first, then decide whether metrics are worth collecting
C. Ask a subagent to guess the likely root cause before any tools run
D. Collect the database metrics twice to verify consistency before reading anything else

**Answer:** A
**Explanation:** Parallelizing independent evidence collection reduces elapsed time without sacrificing completeness. The sequential and guess-first approaches delay or weaken diagnosis, while redundant duplicate collection is not justified by the scenario.

### Q3.
During prompt review, you see an agent issue a directory listing, wait for the response, then read three already-known file paths one by one. What is the clearest performance problem?

A. The agent should never list directories
B. The agent failed to use a subagent for all file work
C. The agent serialized independent reads that could have been emitted together
D. The agent should have written temporary notes before reading files

**Answer:** C
**Explanation:** Once the file paths are known, the reads are independent and should be batched into one response turn. Directory listing may still be useful, subagents are not inherently required, and temporary notes do not address the latency issue.

### Q4.
A coordinator agent must gather the current status of four microservices by calling four health-check tools. One service occasionally times out, but the others usually respond quickly. Why is parallel invocation still preferable?

A. Because a timed-out tool call automatically retries the other three
B. Because one slow dependency should not delay the start of unrelated checks
C. Because parallel calls make health-check results more accurate
D. Because the coordinator loses visibility if it waits on each call individually

**Answer:** B
**Explanation:** Parallel execution prevents a slow or failing service from blocking unrelated observations, reducing total wait time. It does not inherently improve accuracy, remove visibility, or trigger retries for other calls.

### Q5.
An agent is asked to identify whether a bug exists in either the frontend or backend. It chooses to run frontend tests first and backend tests only if the frontend passes, even though the systems are independent. Which exam principle is most directly violated?

A. Context preservation across resumed sessions
B. Goal-oriented delegation to subagents
C. Parallel execution of independent subtasks
D. Restricting tool access for least privilege

**Answer:** C
**Explanation:** The two test runs are independent and should be launched together when possible to reduce overall latency. The other answer choices concern different objectives: resumption, delegation style, and tool restriction.

### Q6.
You are designing an agent loop for a security triage workflow. It needs to pull the dependency manifest, lockfile, and container base-image metadata before deciding on remediation steps. Which output pattern from the agent is best?

A. One tool call that fetches the manifest, followed by a reasoning turn, then two more tool calls
B. Three tool calls emitted together because all inputs are needed before analysis
C. No tool calls; the model should infer likely package versions from memory
D. A single request asking the user to manually paste all three artifacts

**Answer:** B
**Explanation:** Since all three artifacts are independently retrievable and all are required for analysis, emitting them together is the fastest correct design. The alternatives either serialize work or avoid collecting authoritative evidence.

### Q7.
An engineer claims that parallel tool calls are always better than sequential ones. Which scenario is the strongest counterexample?

A. Reading a source file and a separate README
B. Calling a search tool to find a file, then reading the returned path
C. Querying two unrelated monitoring dashboards
D. Fetching three known issue records by ID

**Answer:** B
**Explanation:** The file read depends on the result of the search, so the second step cannot be parallelized safely. The other scenarios involve independent operations that are good candidates for parallel execution.

### Q8.
A coordinator prompt says, "Before every tool call, explain your reasoning in detail to the user." What negative effect is most likely in a parallel-tool-call architecture?

A. It can force unnecessary turn splitting and reduce batching efficiency
B. It guarantees higher-quality explanations after every tool result
C. It prevents the agent from using read-only tools
D. It allows subagents to inherit coordinator memory automatically

**Answer:** A
**Explanation:** Requiring narration before each tool call often causes the agent to break independent work into extra turns instead of batching it. It does not grant tool permissions, improve inheritance, or necessarily improve outcome quality.

### Q9.
An agent must inspect ten tickets from an issue tracker, but API rate limits allow at most three concurrent requests. Which implementation best satisfies the objective while respecting constraints?

A. Fire all ten requests in one turn and ignore the rate limit
B. Read one ticket per turn to avoid complexity
C. Batch requests in groups of up to three concurrent calls
D. Skip tool use and summarize from ticket titles alone

**Answer:** C
**Explanation:** The goal is to maximize safe parallelism, not reckless concurrency. Batching to the allowed concurrency limit reduces latency while honoring system restrictions; the other options either violate constraints or underutilize available parallelism.

### Q10.
While reviewing traces, you notice the agent repeatedly alternates between one search call and one file-read call, even when multiple paths from the search output are already available. What improvement should you recommend?

A. Replace all search calls with manual browsing
B. Emit a single follow-up response containing parallel reads for the relevant paths
C. Add a mandatory summarization step between every file read
D. Force the agent to use only one tool for the entire task

**Answer:** B
**Explanation:** Once the relevant paths are identified, grouping the file reads into one turn reduces additional round trips. The other choices either remove useful tooling or add overhead without solving the batching problem.

### Q11.
An agent must collect CPU, memory, and disk usage from 200 servers. The monitoring tool supports a multi-target request that returns all three metrics per server. What is the best architectural choice?

A. Use the multi-target capability instead of 600 separate serialized calls
B. Query CPU only, then estimate memory and disk from historical averages
C. Ask the user which metric matters most before collecting anything
D. Run 600 sequential requests to make auditing easier

**Answer:** A
**Explanation:** The objective is to reduce total latency through efficient tool usage, and a supported bulk request is even better than many separate calls. The other options either sacrifice correctness or needlessly inflate turnaround time.

### Q12.
Which metric most directly demonstrates that parallel tool-call emission improved an agentic loop?

A. Longer explanations per turn
B. Lower wall-clock time to gather independent evidence
C. More tokens consumed in the system prompt
D. Fewer coordinator-subagent handoffs

**Answer:** B
**Explanation:** The primary benefit of parallelizing independent subtasks is reduced overall latency to obtain required inputs. The other measures may change incidentally, but they do not directly validate the objective.

### Q13.
A model is evaluating a pull request and needs to read `app.py`, `tests/test_app.py`, and `requirements.txt`, all of which are already known. Which prompt instruction most effectively encourages compliant behavior?

A. "Read files only after explaining why each one matters in separate messages."
B. "When multiple known files are relevant and independent, read them in the same response turn."
C. "Start with whichever file seems most important and decide later whether to continue."
D. "Avoid reading tests unless the production file is obviously broken."

**Answer:** B
**Explanation:** This instruction explicitly teaches batching of independent file reads, which is the target behavior. The other prompts either encourage serialization or incomplete evidence gathering.

### Q14.
An observability agent launches four parallel tool calls. Two return enough data to prove the root cause before the other two finish. What is the main architectural advantage of having launched all four at once?

A. The completed calls can be discarded because the other two are still pending
B. The agent can often finish sooner than a serialized design, even if some calls become unnecessary
C. The architecture guarantees that all four responses will arrive in the same order
D. The agent no longer needs to validate conflicting evidence

**Answer:** B
**Explanation:** Parallel execution reduces the chance that late-discovered evidence stalls the diagnosis path; even if some results end up unused, overall elapsed time is often lower. Ordering guarantees and evidence validation are unrelated to the advantage.

### Q15.
You are writing a rubric for evaluating whether an agent properly implements this objective. Which criterion is strongest?

A. The agent always uses at least one tool in every turn
B. The agent issues as many tool calls as possible, regardless of dependency structure
C. The agent batches only independent subtasks whose inputs do not rely on prior tool outputs
D. The agent avoids coordinator summaries until all tool calls in the entire task are complete

**Answer:** C
**Explanation:** Correct parallelization depends on understanding independence, not merely maximizing tool count. Options A, B, and D focus on superficial or counterproductive behaviors rather than safe reduction of round-trip latency.

---

[← Back to objectives index](README.md) · [Back to main index](../../README.md)
