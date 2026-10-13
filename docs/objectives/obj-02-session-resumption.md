# Objective 2: Session Resumption

[← Back to objectives index](README.md) · [Back to main index](../../README.md)

> **Exam objective:** Apply session resumption techniques—including targeted re-analysis of changed files and context injection—to restore agent state accurately without repeating prior work.

---

### Q1.
An agent resumes a previously interrupted refactor session after a teammate has changed only `router.ts` and `auth.ts`. Which recovery plan best fits the objective?

A. Re-read the entire repository to avoid missing anything
B. Reload prior findings, then re-analyze only the changed files and their immediate dependencies
C. Continue coding from memory without checking for changes
D. Discard all prior conclusions because the repo is no longer trustworthy

**Answer:** B
**Explanation:** Effective resumption preserves prior valid work while targeting re-analysis where change actually occurred. Re-reading everything is wasteful, while ignoring updates or discarding all context both reduce accuracy and efficiency.

### Q2.
Why is context injection valuable when resuming a long-running architecture review?

A. It allows the model to overwrite repository files without tool permission
B. It restores key findings, decisions, and open questions so the agent does not rediscover them from scratch
C. It guarantees that no new tool calls will be required
D. It replaces the need to verify whether any files changed

**Answer:** B
**Explanation:** Context injection rehydrates the important state of the task, letting the agent continue from an informed baseline. It does not remove the need for verification, nor does it alter permissions or eliminate all tool use.

### Q3.
An agent resumes work after a test failure from the previous session. The failing stack trace identified `payment_service.py`, but the file has not changed since then. A different file, `currency_utils.py`, changed overnight. What should the agent do first?

A. Ignore the old stack trace because it is stale by definition
B. Re-run the entire test suite before reading any code
C. Re-check the changed utility file and its relationship to the previously failing path
D. Edit `payment_service.py` immediately because it failed last time

**Answer:** C
**Explanation:** Session resumption should combine prior evidence with targeted validation of what changed. Since `currency_utils.py` may influence the old failure path, focused re-analysis is more efficient and accurate than either blind editing or full re-discovery.

### Q4.
Which resume packet provides the most useful context injection for a handoff agent?

A. "We were doing some debugging; please continue."
B. "Last known hypothesis: null token cache in `session_store.go`; verified unaffected files: `api.go`, `routes.go`; pending check: changes in `cache.go` from commit abc123."
C. "The previous model probably handled most of it."
D. "Look around and decide what matters."

**Answer:** B
**Explanation:** A strong resume packet contains concrete findings, verified exclusions, pending questions, and source metadata. The other options are vague and force unnecessary rediscovery.

### Q5.
During session resumption, what is the main purpose of comparing current file state with the files analyzed earlier?

A. To decide whether previous findings remain valid or require partial refresh
B. To prove that the original session was poorly planned
C. To increase total token usage for traceability
D. To avoid ever consulting earlier notes

**Answer:** A
**Explanation:** The comparison step determines what prior reasoning can safely be reused and where fresh analysis is needed. It is not about blame, token inflation, or discarding historical context.

### Q6.
An agent resumes a migration task and receives injected notes that list three completed subtasks and one unresolved schema mismatch. Which action best demonstrates proper resumption?

A. Restart the migration from step one to guarantee consistency
B. Focus on the unresolved schema mismatch and validate whether later changes affect it
C. Delete the injected notes and rely on repo state only
D. Mark the migration done because most subtasks were already completed

**Answer:** B
**Explanation:** Proper resumption picks up from the last unresolved issue while validating whether new changes alter that issue. Restarting wastes effort, deleting useful context loses state, and marking done ignores the remaining problem.

### Q7.
What is the biggest risk of resuming a session without checking for changed files?

A. The model may consume fewer tokens than expected
B. The agent may apply stale conclusions to code that no longer matches earlier analysis
C. The coordinator will automatically revoke tool access
D. The repository history becomes unreadable

**Answer:** B
**Explanation:** Resuming without validating current state can cause the agent to act on outdated assumptions, leading to incorrect edits or recommendations. The other answers are unrelated to resumption integrity.

### Q8.
A coordinator injects prior findings but omits the source metadata showing which files and commits those findings came from. What weakness does this create?

A. The agent cannot distinguish durable conclusions from findings tied to specific older artifacts
B. The agent is forced to use only read-only tools
C. The agent will always over-parallelize tool calls
D. The agent can no longer delegate to subagents

**Answer:** A
**Explanation:** Source metadata anchors prior conclusions to concrete artifacts, making it possible to determine whether those conclusions still apply. Without it, the agent has less confidence about what must be revalidated.

### Q9.
An agent is resuming a documentation update. Only `README.md` changed since the prior session, but the injected context includes earlier analysis of `install.md`, `config.md`, and `deploy.md`. What is the most efficient next step?

A. Re-review all four documents because one changed
B. Reuse prior analysis for unchanged docs and inspect the updated `README.md`
C. Ignore the change because documentation is low risk
D. Rewrite every document section from scratch to keep style consistent

**Answer:** B
**Explanation:** The objective emphasizes avoiding repeated prior work by reusing validated analysis for unchanged files. Only the changed document needs fresh attention unless its edits alter dependencies or referenced content.

### Q10.
Which instruction most effectively improves an agent’s ability to resume accurately?

A. "When resuming, always start over unless the repo is tiny."
B. "Use prior findings as provisional truth, verify changed artifacts, and preserve unchanged validated conclusions."
C. "Never trust notes from earlier sessions."
D. "Continue from the last user message only."

**Answer:** B
**Explanation:** This instruction captures the balance required in session resumption: reuse what remains valid, but verify areas touched by change. The other choices either discard useful state or omit essential verification steps.

### Q11.
A prior session ended after identifying two possible root causes. On resumption, one related file changed and the other did not. What is the best reasoning approach?

A. Treat both hypotheses as equally current until the whole repo is rescanned
B. Immediately dismiss both hypotheses because the session boundary invalidates them
C. Prioritize re-evaluating the hypothesis connected to the changed file while retaining the other as a still-viable candidate
D. Choose the unchanged-file hypothesis because it is more stable

**Answer:** C
**Explanation:** Resumption should update confidence selectively based on what changed. The changed-file hypothesis needs revalidation first, but the unchanged-file hypothesis can remain in scope without forcing a full restart.

### Q12.
Why is a focused diff review often superior to full repository rereads during resumption?

A. It reduces context noise and lets the agent spend attention on potentially invalidated conclusions
B. It eliminates the need for any memory or note-taking
C. It ensures the model will never miss transitive effects
D. It works only for documentation tasks, not code tasks

**Answer:** A
**Explanation:** Targeted diff review keeps the agent’s context budget centered on what likely changed in the problem state. It does not guarantee perfect coverage, but it is usually the best first step when combined with prior findings and dependency awareness.

### Q13.
An agent resumes work on a bug fix and is given injected context that includes "tests not yet run after last code change." What is the correct interpretation?

A. The existing code conclusions are final because the implementation was already written
B. The session can skip validation because the note proves awareness
C. The agent should treat validation as pending work before claiming completion
D. The agent should erase the note because it increases uncertainty

**Answer:** C
**Explanation:** A good resumption process preserves unfinished validation steps as explicit open work items. Awareness of pending tests is not equivalent to having passed them, so completion should not be claimed prematurely.

### Q14.
You are auditing resumption quality. Which behavior is the strongest positive signal?

A. The agent summarizes prior work, identifies changed artifacts, and narrows fresh analysis to areas at risk of invalidating earlier findings
B. The agent repeats every earlier step to ensure exact reproducibility
C. The agent trusts every earlier conclusion and makes edits immediately
D. The agent refuses to resume unless the same model instance is available

**Answer:** A
**Explanation:** This behavior shows accurate state restoration with minimal duplicated effort, which is the heart of the objective. The other choices either waste effort, risk stale reasoning, or impose unnecessary constraints.

### Q15.
What is the clearest reason to include open questions in a resume context package?

A. To give the resumed agent unresolved decision points instead of forcing it to infer what was still pending
B. To prevent the resumed agent from making any new decisions
C. To reduce the need for checking current repository state
D. To guarantee that no earlier finding will be challenged

**Answer:** A
**Explanation:** Open questions tell the resumed agent exactly where prior work stopped and what still requires judgment or evidence. They do not replace current-state verification or freeze the task into an unchangeable plan.

---

[← Back to objectives index](README.md) · [Back to main index](../../README.md)
