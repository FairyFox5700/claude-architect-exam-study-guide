# Objective 8: Agentic review architecture

[← Back to objectives index](README.md) · [Back to main index](../../README.md)

> **Exam objective:** Select the appropriate agentic review architecture—plan mode, direct execution, or multi-phase workflow—based on task scope, risk level, and human approval requirements.

---

### Q1.
A developer asks an agent to update a single typo in a Markdown file and commit the fix on a feature branch. The change is low risk, tightly scoped, and requires no special approval. Which architecture is most appropriate?

A. Plan mode only
B. Direct execution
C. Multi-phase workflow with manual approval between every step
D. Parallel worker swarm with a coordinating planner

**Answer:** B
**Explanation:** The task is simple, low risk, and well specified, so direct execution minimizes overhead while still meeting the goal. Plan mode or multi-phase orchestration would add unnecessary ceremony.

### Q2.
An organization wants to migrate CI pipelines across twelve repositories. The work includes discovery, proposal review by humans, staged implementation, and final validation. Which architecture best fits?

A. Direct execution in one uninterrupted run
B. Plan mode only, with no execution phase
C. Multi-phase workflow
D. A single documentation subagent

**Answer:** C
**Explanation:** Large cross-repository migrations benefit from separate phases for planning, approval, execution, and validation. Direct execution is too risky, and plan mode alone does not complete the requested change.

### Q3.
A user says, "Before touching anything, show me how you would approach cleaning up this unfamiliar deployment script." Which option best matches the request?

A. Plan mode
B. Direct execution
C. Multi-phase workflow that edits first and explains later
D. Parallel direct execution across all scripts

**Answer:** A
**Explanation:** The user explicitly wants an approach before any changes are made, which is the core use case for plan mode. Direct execution would violate the requested approval boundary.

### Q4.
A production outage is traced to a known one-line configuration mistake. However, company policy requires validation evidence and human approval before any production-facing fix is applied. Which architecture is best?

A. Direct execution because the fix is small
B. Plan mode only because production changes are never implemented by agents
C. Multi-phase workflow with diagnosis, validation, approval, and execution stages
D. Pure parallel execution by multiple workers with no gating

**Answer:** C
**Explanation:** Even a tiny change becomes high risk when the environment is sensitive and formal approval is required. A multi-phase workflow supports evidence gathering and gated execution without skipping controls.

### Q5.
A platform team wants an agent to inspect an unfamiliar repository and recommend whether the test strategy should be modernized. They do not want any changes yet. Which architecture is most suitable?

A. Direct execution
B. Plan mode
C. Multi-phase workflow with mandatory code edits
D. Sequential pipeline that auto-merges improvements

**Answer:** B
**Explanation:** The goal is exploratory assessment and recommendation, not immediate implementation, so plan mode is the best fit. It allows analysis without crossing into modification.

### Q6.
A user requests a straightforward update to two documentation links and asks the agent to make the edits now. There are no approvals, downstream systems, or hidden dependencies involved. What is the best architecture?

A. Direct execution
B. Plan mode
C. Multi-phase workflow with a handoff to a review board
D. Coordinator-worker architecture with five parallel reviewers

**Answer:** A
**Explanation:** Small, low-risk documentation edits are ideal for direct execution. Additional phases would slow the task without improving safety meaningfully.

### Q7.
A regulated workflow requires a design proposal, stakeholder sign-off, implementation, and independent verification before closing the task. Which architecture most clearly supports those constraints?

A. Direct execution with a long prompt
B. Plan mode only
C. Multi-phase workflow
D. Single-pass summarization

**Answer:** C
**Explanation:** The required checkpoints map naturally to distinct phases with explicit transitions and approvals. Direct execution and plan-only modes do not support full lifecycle control.

### Q8.
A test suite fails because of an obvious null dereference in one function. The engineer asks the agent to fix it and rerun the affected tests immediately. Which choice is best?

A. Plan mode because all code changes should be preplanned
B. Direct execution because the scope is narrow and the desired action is explicit
C. Multi-phase workflow because every bug fix requires human gating
D. No architecture can safely handle this task

**Answer:** B
**Explanation:** The task is well defined, localized, and includes a clear validation step, making direct execution efficient and appropriate. Plan mode would be slower without adding significant risk reduction.

### Q9.
An agent is asked to "improve reliability across our deployment tooling" without further detail. The repository contains multiple scripts, cloud templates, and environment-specific overrides. Which starting architecture is most appropriate?

A. Direct execution because the user asked for improvement
B. Plan mode to clarify scope, identify risks, and propose a path before changes
C. Multi-phase workflow that begins by editing every deployment file
D. Sequential execution of a canned checklist regardless of repository findings

**Answer:** B
**Explanation:** The request is broad and ambiguous, so the agent should first develop a scoped plan rather than making assumptions and editing widely. Plan mode reduces risk by surfacing unknowns before action.

### Q10.
A security team wants an agent to investigate potential secrets exposure, present findings, and only then remediate after explicit approval. Which architecture best fits?

A. Direct execution
B. Plan mode only
C. Multi-phase workflow with a findings phase and a separate remediation phase
D. Pure parallel execution with no state between phases

**Answer:** C
**Explanation:** The required separation between investigation and later remediation is a textbook case for multi-phase architecture. Plan mode alone stops too early, while direct execution merges activities that policy wants separated.

### Q11.
A user asks, "Give me the safest sequence to refactor this service, but do not modify code yet because I need to review it with the team." Which architecture should you choose?

A. Direct execution
B. Multi-phase workflow with immediate implementation
C. Plan mode
D. Parallel workers editing separate modules simultaneously

**Answer:** C
**Explanation:** The user specifically requests a safe sequence for review before any changes occur. Plan mode is designed for exactly that kind of advisory, pre-implementation work.

### Q12.
A repository-wide rename affects 200 files, generated code, and CI references. The organization wants a dry run, human review, then controlled execution and validation. What is the best architecture?

A. Direct execution because renames are mechanically simple
B. Plan mode only because bulk changes should never be applied
C. Multi-phase workflow
D. Single-worker direct editing without validation

**Answer:** C
**Explanation:** Large blast-radius changes need explicit staging, review, and validation, even if the edits themselves are mechanical. A multi-phase approach manages scope and approval safely.

### Q13.
An operator says, "I am not sure whether this issue is even actionable. First tell me what you would inspect and what data you need." Which architecture is best aligned?

A. Direct execution
B. Plan mode
C. Multi-phase workflow with automatic remediation
D. Parallel execution across all services immediately

**Answer:** B
**Explanation:** When the first need is to determine actionability and required data, planning and scoping come before execution. Plan mode captures that discovery-oriented first step.

### Q14.
A user wants an agent to reformat a single local JSON configuration file before uploading it to another tool. No approvals are needed, and the outcome is easily verifiable. Which architecture is most appropriate?

A. Direct execution
B. Plan mode
C. Multi-phase workflow with review committee approval
D. Distributed worker pool with a coordination layer

**Answer:** A
**Explanation:** This is a narrow, low-risk, immediately executable task with simple validation. Direct execution is the most efficient architecture for such work.

### Q15.
A build-system migration must include an initial assessment, a draft proposal, a human sign-off, a staged rollout, and a post-migration verification report. Which architecture is the best fit?

A. Plan mode only
B. Direct execution
C. Multi-phase workflow
D. Uncoordinated parallel execution

**Answer:** C
**Explanation:** The task explicitly contains multiple lifecycle stages with required human approval between them. Multi-phase workflows are designed to preserve that structure and risk control.

---

[← Back to objectives index](README.md) · [Back to main index](../../README.md)
