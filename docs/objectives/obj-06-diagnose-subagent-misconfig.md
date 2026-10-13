# Objective 6: Diagnose subagent misconfiguration

[← Back to objectives index](README.md) · [Back to main index](../../README.md)

> **Exam objective:** Diagnose misconfigured subagent spawning by identifying missing tool permissions, incorrect AgentDefinition parameters, or absent coordinator-to-subagent wiring.

---

### Q1.
A coordinator can browse documentation successfully, but every spawned research subagent fails immediately with `permission denied: web_fetch`. The child agent receives the correct task prompt and starts normally. What is the most likely root cause?

A. The coordinator prompt is too vague for the research task
B. The subagent's tool permissions do not include `web_fetch`
C. The coordinator should have used a sequential pipeline instead of delegation
D. The child agent needs a larger context window before using network tools

**Answer:** B
**Explanation:** The failure is specific to the child agent and names a blocked tool, which points directly to missing child permissions. Prompt quality, architecture choice, and context size would not produce a deterministic permission-denied error for a single tool.

### Q2.
An implementation coordinator spawns a test-runner subagent after generating code changes. The subagent starts, but its logs show `shell tool unavailable`, and no tests run. The AgentDefinition for that child lists only `filesystem` and `view`. Which fix best addresses the issue?

A. Add shell execution permission to the child AgentDefinition
B. Increase the subagent timeout so the shell can initialize
C. Move test execution back into the coordinator prompt
D. Replace the test runner with a documentation subagent

**Answer:** A
**Explanation:** The child was assigned a task requiring command execution, but its declared tool set does not include a shell-capable tool. Timeout changes and prompt reshuffling do not solve a capability mismatch created by the AgentDefinition.

### Q3.
A planner agent detects a potential secrets exposure and emits an event named `security_review_requested`. The architecture document says this event should trigger a specialized security subagent, but no child is ever created. Logs show the detector event is emitted successfully. What is the best diagnosis?

A. The security subagent prompt is too long to execute
B. The system lacks coordinator-to-subagent wiring from the detector event to the spawn action
C. The issue is caused by excessive parallelism in the worker pool
D. The child agent needs a different temperature setting

**Answer:** B
**Explanation:** If the triggering event exists but no child is spawned, the missing link is usually the orchestration wiring that converts the event into a spawn call. Prompt length and temperature tuning do not explain the absence of any spawn attempt.

### Q4.
A repository-analysis subagent is supposed to inspect `package.json` files under the active workspace. Instead, it fails with `file not found` because it launches in a default home directory. Which configuration error is most likely?

A. The coordinator omitted the working-directory parameter when spawning the child
B. The child model should be switched to a larger reasoning model
C. The repository should be copied into the child prompt as plain text
D. The coordinator should always run file discovery itself

**Answer:** A
**Explanation:** When a child agent cannot find expected workspace files and starts in the wrong location, the most likely issue is an incorrect or missing working-directory parameter. Model size and prompt-copying do not fix incorrect execution context.

### Q5.
A coordinator spawns an approval-gated remediation subagent in a non-interactive environment. The child waits forever in a `pending approval` state even though the parent session is configured for autonomous execution. What is the best explanation?

A. The child's approval mode is incompatible with the runtime and requires interactive confirmation
B. The child needs more CPU resources before it can continue
C. The coordinator should split the remediation into smaller prompts
D. The parent must retry the same spawn call three times

**Answer:** A
**Explanation:** A child configured to require interactive approvals will stall in a non-interactive environment. Resource allocation and prompt granularity do not resolve a policy mismatch between the child configuration and the execution environment.

### Q6.
A workflow tries to launch a reviewer subagent with type `code-reviewer`, but the runtime only recognizes `code-review`. Spawn attempts fail before the child starts. Which category best describes this failure?

A. Missing coordinator-to-subagent wiring
B. Incorrect AgentDefinition parameter
C. Missing tool permission
D. Excessive state persistence overhead

**Answer:** B
**Explanation:** The child cannot be instantiated because a required definition parameter uses an invalid agent type value. No tool is even invoked yet, so this is not a permission problem, and the spawn path itself exists, so it is not a wiring issue.

### Q7.
A research subagent needs an API token that the coordinator can access through its environment. The child launches correctly and has the right tools, but every outbound request returns `unauthorized` because the token is missing from the child runtime. What is the most likely fix?

A. Increase the number of retries in the research loop
B. Inherit or explicitly pass the required environment configuration to the subagent
C. Disable state persistence for the child
D. Convert the task into a pure plan-mode workflow

**Answer:** B
**Explanation:** The symptom shows the child lacks required runtime configuration even though permissions and prompts are fine. Retries and architectural changes will not make a missing credential appear in the child environment.

### Q8.
A coordinator creates a summarizer subagent after a scan completes. The child starts and exits immediately with a generic summary because the prompt template references `{{scan.findings}}`, but the coordinator provides only `scan_results`. What is the strongest diagnosis?

A. The child needs additional file-system permissions
B. The coordinator and child are miswired through incompatible payload fields
C. The summarizer should run in parallel with the scan
D. The scan tool is misconfigured and must be replaced

**Answer:** B
**Explanation:** The child is being spawned, but the expected input field is absent or renamed, so the handoff wiring between producer and consumer is incorrect. Tool permissions and scan replacement are unrelated to the missing payload mapping.

### Q9.
A planner chooses a lightweight child profile for dependency analysis. The profile can read files but cannot execute package-manager commands needed to resolve transitive dependencies, so the task fails halfway through. Which remediation is best?

A. Keep the profile and ask the child to reason harder
B. Select a child definition whose capabilities match the operational requirements
C. Remove dependency analysis from the workflow entirely
D. Force the coordinator to summarize installed packages from memory

**Answer:** B
**Explanation:** The child profile is misconfigured because its capabilities do not match the assigned task. Better prompting cannot compensate for missing operational abilities such as required tool access.

### Q10.
A coordinator spawns three worker subagents and stores their IDs in `pending_workers`. Completion callbacks, however, look up results in `active_children`, which is never populated. The coordinator keeps waiting even though the workers finished. What is the best diagnosis?

A. The workers were created with the wrong reasoning model
B. The coordinator lacks correct result-collection wiring for the spawned children
C. The workers need broader file permissions
D. The coordinator should switch to direct execution

**Answer:** B
**Explanation:** The subagents run successfully, but the coordinator does not connect their completions to the correct tracking structure. That is a handoff and correlation problem, not a model or permission problem.

### Q11.
A report-writer subagent is supposed to read an artifact produced by an analyzer child. The artifact exists, and the path is correct, but the writer receives `access denied` when opening it. The parent can read the file without issue. What is the most likely cause?

A. The analyzer produced malformed output
B. The report writer lacks the required file-access permission or mount scope
C. The writer prompt should contain the entire artifact inline instead
D. The coordinator should convert the workflow to plan mode

**Answer:** B
**Explanation:** The artifact is present and readable by the parent, so the remaining likely fault is restricted child access to that location. Inline prompts and architectural changes are workarounds, not the direct fix.

### Q12.
A child agent starts and repeatedly states it is waiting for assignment details. Inspection shows the spawn call includes the agent type and tools but omits the actual task payload. Which answer best identifies the failure?

A. Missing initial coordinator-to-subagent handoff data
B. Incorrect context-window size for the child model
C. Insufficient persistence checkpoints
D. Excessive concurrency in the worker pool

**Answer:** A
**Explanation:** A child that launches but lacks actionable instructions has usually been spawned without the required assignment content. Context size and checkpoint strategy matter later, but they do not explain an empty initial task.

### Q13.
In production, a child launch fails with `tool not registered: repo-search`, even though staging worked. The coordinator requests `repo-search`, but the production runtime exposes the tool as `code-search`. What should you diagnose first?

A. A missing memory checkpoint in the coordinator
B. A naming mismatch between the requested tool and the runtime tool registry
C. A need to raise worker parallelism to compensate
D. A malformed markdown report template

**Answer:** B
**Explanation:** The error directly indicates that the coordinator or AgentDefinition references a tool name the runtime does not recognize. Parallelism and reporting templates are unrelated to a failed tool lookup at launch time.

### Q14.
A multi-step workflow spawns a remediation child only if the planner marks an issue as `actionable`. After a schema change, the planner now emits `ready_for_fix`, and remediation never starts. Which option best explains the breakage?

A. The remediation child lost access to write files
B. The planner should be given more tokens to think
C. The coordinator's trigger wiring no longer matches the planner's output schema
D. The remediation child must be retrained on the repository

**Answer:** C
**Explanation:** The child launch condition depends on a specific output field or status value, and that contract changed. This is a classic wiring failure caused by an incompatible producer-consumer schema.

### Q15.
An analysis child finishes successfully, but the downstream report child sees an empty input object because the coordinator spawns it before persisting or forwarding the analysis result reference. What is the best corrective action?

A. Add explicit dependency handling so the report child starts only after the analysis output is stored and passed forward
B. Increase the report child's temperature to encourage better inference
C. Remove the analysis step and let the report child inspect the repository directly
D. Shorten the report prompt to reduce latency

**Answer:** A
**Explanation:** The downstream child depends on output that was neither durably recorded nor correctly forwarded before launch. Synchronizing the dependency and passing the produced reference fixes the handoff at the source.

---

[← Back to objectives index](README.md) · [Back to main index](../../README.md)
