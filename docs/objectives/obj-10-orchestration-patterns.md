# Objective 10: Orchestration patterns

[← Back to objectives index](README.md) · [Back to main index](../../README.md)

> **Exam objective:** Evaluate multi-agent orchestration patterns—coordinator-worker, parallel execution, and sequential pipelines—to select the structure best satisfying research coverage, latency, and reliability requirements.

---

### Q1.
A research team must gather evidence from eight unrelated external sources under a tight deadline. Each source can be queried independently, and the main concern is minimizing total elapsed time. Which orchestration pattern is the best fit?

A. Sequential pipeline
B. Parallel execution
C. Coordinator-worker with serialized approvals on every source
D. Single-agent direct execution

**Answer:** B
**Explanation:** When tasks are independent and latency matters most, parallel execution reduces wall-clock time by working on all sources concurrently. A sequential pipeline would unnecessarily serialize the work.

### Q2.
A document-processing system must first extract raw text, then classify the content, then generate a report based on the classification output. Each stage depends on the previous stage's result. Which pattern is most appropriate?

A. Parallel execution
B. Coordinator-worker with no defined order
C. Sequential pipeline
D. Unstructured worker swarm

**Answer:** C
**Explanation:** The stages have clear dependencies, so a sequential pipeline is the natural structure. Parallel execution would add complexity without removing the dependency chain.

### Q3.
A lead agent needs to assign different specialists to investigate authentication, deployment, and observability concerns, then merge their findings and fill any gaps. Which pattern best supports this behavior?

A. Coordinator-worker
B. Pure sequential pipeline
C. Single-threaded direct execution
D. Static documentation generation

**Answer:** A
**Explanation:** A coordinator-worker pattern is ideal when a central planner delegates different scopes, tracks coverage, and integrates results. Pure parallel execution lacks the same explicit control over gap detection and follow-up assignment.

### Q4.
A data-enrichment job must call four slow external APIs for each record, but the API calls do not depend on one another. The SLA is dominated by response time. Which pattern is best?

A. Sequential pipeline
B. Parallel execution
C. Coordinator-worker only if there is exactly one worker
D. Manual-only orchestration

**Answer:** B
**Explanation:** Independent slow operations are classic candidates for parallel execution because concurrency reduces end-to-end latency. A sequential pipeline would compound the external wait times.

### Q5.
A system distributes hundreds of homogeneous analysis tasks. Some workers may fail, and the design must support retries, reassignment, and centralized progress tracking. Which pattern is the best choice?

A. Coordinator-worker
B. Pure sequential pipeline
C. Direct execution by one agent
D. Plan mode with no workers

**Answer:** A
**Explanation:** Coordinator-worker architectures excel when many units of work need scheduling, retry logic, and consolidated visibility. Pure parallel execution without coordination makes reliability controls harder to enforce.

### Q6.
A publishing workflow must redact PII, then perform legal review, then generate a public summary. Later stages must never run on unredacted input. Which pattern best fits?

A. Parallel execution
B. Sequential pipeline
C. Coordinator-worker with no stage boundaries
D. Worker swarm chosen randomly at runtime

**Answer:** B
**Explanation:** Strict ordering and transformation dependencies make a sequential pipeline the safest pattern. Running stages in parallel would violate the required processing guarantees.

### Q7.
You need to classify 500 independent documents as quickly as possible, and each classification task is self-contained. Coverage is already ensured by the document list itself. Which pattern is most efficient?

A. Sequential pipeline
B. Parallel execution
C. Coordinator-worker with interactive approvals for each document
D. A single large summarization prompt

**Answer:** B
**Explanation:** Self-contained, uniform work items with no cross-item dependencies are ideal for parallel execution. Adding a heavy coordinator can help at scale, but the defining pattern for latency here is broad parallelism.

### Q8.
A threat-hunting workflow must explore leads that appear during execution, assign follow-up tasks dynamically, and stop only when the coordinator judges coverage sufficient. Which pattern best matches this requirement?

A. Sequential pipeline
B. Parallel execution with no central control
C. Coordinator-worker
D. Static batch processing only

**Answer:** C
**Explanation:** Dynamic branching, gap analysis, and adaptive delegation are strengths of coordinator-worker systems. A simple parallel pool does not provide the same decision-making structure for evolving investigations.

### Q9.
A workflow has three mandatory stages—inventory, validation, and reporting—but within the validation stage, many checks can run concurrently. Which overall orchestration pattern is still the best primary description?

A. Sequential pipeline
B. Pure coordinator-worker with no stage ordering
C. Parallel execution only
D. Unmanaged worker mesh

**Answer:** A
**Explanation:** The workflow is primarily structured by ordered stages, even if one stage contains internal parallelism. Its top-level architecture remains a sequential pipeline because downstream steps depend on completion of earlier phases.

### Q10.
A compliance team values reproducibility and explicit stage gates more than raw speed. Each stage must verify outputs before the next stage begins. Which pattern should be preferred?

A. Parallel execution
B. Sequential pipeline
C. Coordinator-worker optimized for rapid reassignment
D. Opportunistic best-effort parallel scanning

**Answer:** B
**Explanation:** Sequential pipelines provide clear checkpoints and deterministic ordering, which aligns well with compliance-driven reproducibility. Parallel execution prioritizes speed, not strong stage boundaries.

### Q11.
A batch of independent repository searches should not be blocked by one slow or failed search task. The main objective is keeping overall throughput high. Which pattern is best?

A. Sequential pipeline
B. Parallel execution
C. Manual serial review
D. Single-worker coordinator pattern

**Answer:** B
**Explanation:** Parallel execution isolates slow tasks so they do not hold up unrelated work, improving aggregate throughput. Serial approaches let the slowest unit dominate total completion time.

### Q12.
A team notices that a central coordinator has become a bottleneck for a small, fixed three-step process with no branching and no dynamic assignment needs. Which alternative pattern is likely better?

A. Coordinator-worker with more coordinators
B. Sequential pipeline
C. Parallel execution of all three dependent steps at once
D. Unstructured multi-agent debate

**Answer:** B
**Explanation:** For a short fixed dependency chain, a sequential pipeline removes unnecessary coordination overhead while preserving correctness. Adding more coordinators would increase complexity without solving the fundamental mismatch.

### Q13.
An architecture review needs topic specialists to cover storage, networking, identity, and observability. After initial results, one central agent must identify uncovered risks and dispatch more follow-up work. Which pattern is strongest?

A. Pure sequential pipeline
B. Pure parallel execution with no aggregation logic
C. Coordinator-worker
D. One-shot direct execution

**Answer:** C
**Explanation:** The need for both specialist parallelism and central gap management is a hallmark of coordinator-worker orchestration. Pure parallelism alone lacks the explicit mechanism for coverage assessment and follow-up delegation.

### Q14.
A reporting workflow compares three candidate patterns for a new system. The task is to minimize latency for independent evidence gathering while preserving a single place to reconcile duplicates and conflicts. Which pattern best satisfies both goals?

A. Sequential pipeline
B. Coordinator-worker
C. Direct execution by one agent
D. No orchestration pattern can satisfy both requirements

**Answer:** B
**Explanation:** Coordinator-worker allows many workers to gather evidence concurrently while a central coordinator deduplicates, reconciles, and directs additional investigation. Pure parallel execution improves latency but gives weaker built-in control over conflict handling and coverage.

### Q15.
An environment has intermittent worker failures and uneven task durations. The design must support work stealing, retries, and centralized visibility into incomplete tasks. Which pattern is the best fit?

A. Sequential pipeline
B. Parallel execution with no ownership tracking
C. Coordinator-worker
D. Static direct execution with no delegation

**Answer:** C
**Explanation:** Coordinator-worker patterns are best suited for reliability features such as retry queues, work redistribution, and global progress tracking. A bare parallel model without coordination struggles to manage these failure-handling requirements cleanly.

---

[← Back to objectives index](README.md) · [Back to main index](../../README.md)
