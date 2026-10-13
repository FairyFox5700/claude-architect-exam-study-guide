# Objective 4: Delegation Strategies

[← Back to objectives index](README.md) · [Back to main index](../../README.md)

> **Exam objective:** Evaluate subagent delegation strategies—goal-oriented versus procedural instructions—and select the approach that enables adaptive behavior while maintaining coordinator visibility and control.

---

### Q1.
A coordinator can instruct a subagent either with a strict step-by-step procedure or with a goal and success criteria. When is the goal-oriented style generally superior?

A. When the task may require adaptive investigation paths based on what the subagent discovers
B. When the coordinator wants to hide the task outcome from the subagent
C. When tool access has not been configured yet
D. When the coordinator does not know the task well enough to describe it at all

**Answer:** A
**Explanation:** Goal-oriented delegation is most valuable when the subagent must adapt its approach to emerging evidence while still aiming at a defined outcome. It is not a substitute for scoping, tool setup, or basic task clarity.

### Q2.
Which delegation prompt best balances adaptability with coordinator control?

A. "Run these exact 19 commands in this exact order, even if earlier results make later steps irrelevant."
B. "Determine whether the cache invalidation bug still exists in `cache_manager.ts`; use the provided diff and report the evidence chain and final conclusion."
C. "Do whatever seems helpful and send me something interesting."
D. "Fix all bugs in the repository."

**Answer:** B
**Explanation:** This prompt specifies the goal, scope, and reporting expectations while leaving the subagent flexibility in method. The procedural prompt overconstrains behavior, while C and D are too vague for controlled delegation.

### Q3.
Why can overly procedural delegation be a liability in dynamic debugging tasks?

A. It can prevent the subagent from adapting when tool results invalidate the planned sequence
B. It always increases security risk
C. It removes the need for coordinator review
D. It guarantees higher token usage than goal-oriented prompts

**Answer:** A
**Explanation:** When evidence changes the right next step, rigid procedures can lock the subagent into inefficient or incorrect actions. Security risk and token count are contextual, not guaranteed outcomes.

### Q4.
In which scenario is a more procedural delegation style justified?

A. A broad exploratory architecture assessment with many unknowns
B. A repeatable compliance checklist where every required check must be performed in a known order
C. A root-cause investigation with several competing hypotheses
D. A performance triage where the subagent may need to branch based on metrics

**Answer:** B
**Explanation:** Procedural instructions fit deterministic workflows where completeness depends on executing a fixed checklist. Exploratory and branching tasks benefit more from goal-oriented flexibility.

### Q5.
What is the key difference between a goal-oriented delegation and an underspecified delegation?

A. Goal-oriented delegation defines the desired outcome and boundaries; underspecified delegation leaves the subagent guessing what success looks like
B. Goal-oriented delegation never mentions tools
C. Goal-oriented delegation always takes fewer tokens
D. Goal-oriented delegation prevents all intermediate reporting

**Answer:** A
**Explanation:** Good goal-oriented prompts are not vague—they clearly state success criteria while allowing method flexibility. The other answers confuse delegation style with token count, tool usage, or reporting design.

### Q6.
A coordinator wants visibility into a subagent’s work without micromanaging every step. Which instruction is best?

A. "Follow my exact step list and do not deviate."
B. "Investigate the memory leak, and include the evidence path, tools used, and final recommendation in your report."
C. "Just fix it."
D. "Ask me before every tool call."

**Answer:** B
**Explanation:** Requiring a transparent report preserves coordinator visibility while still allowing adaptive execution. Asking before every tool call or prescribing every action reduces efficiency and autonomy.

### Q7.
An architecture team notices that subagents often miss better approaches because prompts dictate command order too rigidly. What change is most appropriate?

A. Remove all task scoping so subagents can improvise freely
B. Shift from step-by-step command instructions to objective-driven prompts with constraints and output expectations
C. Ban delegation for all debugging tasks
D. Increase the number of mandatory coordinator checkpoints after every command

**Answer:** B
**Explanation:** The problem is overconstraint, not delegation itself. Moving to goal-oriented prompts preserves scope while allowing the subagent to choose better tactics based on evidence.

### Q8.
Which prompt most clearly reflects procedural delegation rather than goal-oriented delegation?

A. "Decide whether the retry logic can cause duplicate charges and explain your conclusion."
B. "Open `payments.ts`, inspect lines 1-200, then read `queue.ts`, then run the retry test, then summarize."
C. "Assess the rollback risk for the new payment worker using the attached traces."
D. "Determine whether the observed timeout comes from the database or the queue."

**Answer:** B
**Explanation:** This prompt prescribes a specific sequence of actions rather than defining an end state and letting the subagent select the best path. The others are centered on goals and conclusions.

### Q9.
What is the main coordinator benefit of a well-designed goal-oriented delegation?

A. The coordinator receives outcome-focused results while the subagent adapts locally to evidence
B. The coordinator never needs to review the subagent’s conclusions
C. The coordinator can skip providing any prior findings
D. The coordinator loses visibility but gains speed

**Answer:** A
**Explanation:** Goal-oriented delegation lets the coordinator stay focused on intent and results rather than operational minutiae, while still retaining oversight through scoped tasks and reporting. It does not remove the need for review or context.

### Q10.
A subagent is reviewing a diff where the exact investigative path depends on whether the bug is in input validation or retry logic. Which delegation style is best?

A. Goal-oriented, because the subagent may need to branch based on what it finds
B. Procedural, because all diff reviews should follow the same ordered recipe
C. Neither; delegation is inappropriate for diff analysis
D. Procedural, but only if the coordinator is uncertain

**Answer:** A
**Explanation:** Branching investigative tasks benefit from prompts that define the goal and scope without locking the subagent into a single path. A rigid recipe may waste time or miss the most relevant evidence trail.

### Q11.
When might a hybrid strategy be best?

A. When the coordinator specifies a goal plus a few mandatory checks, while leaving the rest of the approach flexible
B. When the coordinator wants to avoid giving any success criteria
C. When the coordinator prefers the subagent to invent its own scope
D. When tool restrictions are impossible to apply

**Answer:** A
**Explanation:** A hybrid strategy combines required checkpoints with room for adaptation, which is often ideal for high-stakes but non-deterministic tasks. The other options reflect poor scoping, not a deliberate delegation strategy.

### Q12.
Which instruction would most likely reduce adaptive behavior unnecessarily?

A. "Report only high-confidence findings from the attached scope."
B. "Use the provided benchmarks, but choose the best analysis path."
C. "Execute the following exact sequence regardless of what the first result shows."
D. "Determine whether the rollback plan is sufficient."

**Answer:** C
**Explanation:** Forcing an exact sequence regardless of evidence removes the subagent’s ability to respond intelligently to what it learns. The other prompts constrain outputs or scope without eliminating adaptability.

### Q13.
An agent coordinator is concerned that a goal-oriented prompt might reduce visibility. What is the best mitigation?

A. Replace it with a fully procedural script in all cases
B. Add reporting requirements such as evidence summary, decision rationale, and unresolved risks
C. Remove delegation entirely
D. Tell the subagent to be transparent without defining the task

**Answer:** B
**Explanation:** Visibility is preserved through structured outputs and scoped reporting, not by eliminating adaptability altogether. Full procedural control is only warranted when the task itself is procedural.

### Q14.
Which example best demonstrates poor delegation strategy selection?

A. Using a checklist-style prompt for a deterministic audit
B. Using a goal-oriented prompt for an exploratory failure analysis
C. Using a rigid command sequence for a task whose next step depends on live findings
D. Using a hybrid prompt for a migration with mandatory validations

**Answer:** C
**Explanation:** A dynamic task with branching outcomes is exactly where rigid sequencing performs poorly. The other options match delegation style to task shape more appropriately.

### Q15.
What should an exam candidate remember when choosing between goal-oriented and procedural delegation?

A. Procedural is always safer because it reduces thinking
B. Goal-oriented is always better because it sounds more autonomous
C. Match the instruction style to the task: use goals for adaptive work and procedures for fixed, repeatable workflows
D. Avoid mixed strategies because they confuse all subagents

**Answer:** C
**Explanation:** The correct choice depends on whether the task is exploratory or deterministic. Neither style is universally best; strong architecture selects the one that preserves both effectiveness and coordinator control.

---

[← Back to objectives index](README.md) · [Back to main index](../../README.md)
