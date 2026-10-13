# Objective 3: Subagent Prompt Completeness

[← Back to objectives index](README.md) · [Back to main index](../../README.md)

> **Exam objective:** Construct subagent prompts that include all findings, structured data, and source metadata required for task completion without returning to the coordinator for missing context.

---

### Q1.
A coordinator asks a subagent to finish a regression analysis but provides only, "Please continue investigating the login bug." Which deficiency most directly violates the objective?

A. The prompt lacks complete context, findings, and source references needed for autonomous completion
B. The prompt uses too few tokens, which always lowers model quality
C. The prompt should have included tool restrictions instead of task details
D. The prompt incorrectly delegates any debugging work at all

**Answer:** A
**Explanation:** A complete subagent prompt must contain the necessary state so the subagent does not need to return for missing background. Token count alone is not the issue, and delegation may be valid if the context is sufficient.

### Q2.
Which prompt is most likely to let a subagent complete a code review without asking the coordinator for missing context?

A. "Review the recent changes and report issues."
B. "Review `billing.py` and `tests/test_billing.py` from commit `9f2c1d`; prior findings: flaky rounding test already explained by locale mismatch, do not re-investigate; focus on newly added refund path and use attached diff summary."
C. "Find anything interesting in the repository."
D. "Start wherever you want and ask me if you get confused."

**Answer:** B
**Explanation:** This prompt includes scope, source metadata, prior findings, exclusions, and a concrete focus area, enabling the subagent to operate independently. The other prompts are underspecified and invite avoidable round trips.

### Q3.
Why is source metadata important in a subagent handoff?

A. It tells the subagent which earlier conclusions map to which files, commits, or artifacts
B. It allows the subagent to bypass coordinator oversight entirely
C. It guarantees that the subagent will not need tool access
D. It replaces the need to define the task outcome

**Answer:** A
**Explanation:** Source metadata anchors findings to evidence, helping the subagent assess relevance and currency. It does not remove the need for outcome definition, tool use, or coordinator control.

### Q4.
A coordinator passes a table of service latencies to a subagent but omits the units and collection window. What is the main architectural problem?

A. The prompt contains structured data but lacks critical metadata required to interpret it correctly
B. The subagent can infer units from the largest number
C. Units matter only for dashboards, not for agents
D. The coordinator should have converted the table into prose to avoid ambiguity

**Answer:** A
**Explanation:** Structured data without interpretive metadata can be misleading or unusable. Converting to prose does not inherently solve missing units or timestamps, and inference is unsafe when precise analysis is required.

### Q5.
A subagent needs to decide whether a deployment can proceed. Which prompt component is most essential for autonomy?

A. A reminder that the coordinator is very busy
B. A clear completion criterion such as "determine whether the canary failure blocks rollout"
C. An apology for limited context
D. A request to be concise

**Answer:** B
**Explanation:** Subagents need a defined objective and stopping condition so they can act independently and know when the task is complete. Tone and brevity instructions are secondary and do not substitute for mission clarity.

### Q6.
You are handing off a security triage to a subagent. Which package best satisfies the completeness objective?

A. "Check for security issues in auth."
B. "Investigate authentication changes in `auth_handler.rs` from PR #482. Known facts: token expiry bug is already confirmed non-exploitable; attached list of modified functions and request samples; report only high-confidence exploitable findings."
C. "Security review the whole repo and let me know what happens."
D. "You probably know what auth problems look like."

**Answer:** B
**Explanation:** This prompt defines scope, source, prior findings, available evidence, and reporting criteria. The alternatives force the subagent to rediscover basics or operate without adequate boundaries.

### Q7.
What is the strongest reason to include "already ruled out" hypotheses in a subagent prompt?

A. To reduce duplicate investigation and keep the subagent focused on unresolved paths
B. To ensure the subagent never questions earlier work
C. To shorten the prompt by removing all uncertainty
D. To eliminate the need for source metadata

**Answer:** A
**Explanation:** Explicitly stating ruled-out paths prevents wasted effort and unnecessary re-analysis. It should guide focus, not forbid all re-evaluation when new evidence emerges.

### Q8.
A coordinator gives a subagent a CSV extract and says, "Find anomalies." The subagent returns asking what each column means. How could this have been prevented?

A. By restricting the subagent to read-only tools
B. By including schema definitions, time range, and any relevant business meaning for the columns
C. By telling the subagent to be more proactive
D. By removing the CSV and sending only a high-level summary

**Answer:** B
**Explanation:** Complete prompts include not just data but the metadata needed to interpret that data. Tool restrictions or personality cues do not replace schema and semantic context.

### Q9.
Which omission is most likely to force an unnecessary coordinator-subagent round trip?

A. Not specifying whether the final answer should include code snippets or only findings
B. Using bullet points instead of numbered lists
C. Including too much source metadata
D. Stating the objective too clearly

**Answer:** A
**Explanation:** Output format requirements affect whether the subagent can finish in one pass or must request clarification. The other options are either harmless or beneficial to completion.

### Q10.
An agent prompt includes detailed findings but no explicit list of artifacts the findings came from. What failure mode is most likely?

A. The subagent may be unable to tell whether the findings apply to the current scope or need revalidation
B. The subagent will always ignore the findings
C. The subagent will gain access to unauthorized files
D. The subagent will overuse parallel tool calls

**Answer:** A
**Explanation:** Without artifact linkage, findings lose traceability and are harder to apply safely. That increases clarification pressure and the chance of either redundant or stale analysis.

### Q11.
Which coordinator instruction most directly improves prompt completeness for a subagent summarizing benchmark results?

A. "Use your judgment."
B. "The attached benchmark table covers build times on Windows runners over the last 14 days; columns are median seconds, p95 seconds, and cache-hit ratio; compare only services changed in commit range `a1b2..d4e5`."
C. "You should be able to figure it out."
D. "Please be fast."

**Answer:** B
**Explanation:** This instruction supplies the structured data context, time window, definitions, and source range needed for precise analysis. The other options provide almost no operational guidance.

### Q12.
A coordinator wants a subagent to patch a bug in a specific function. Which additional detail best supports a one-shot completion?

A. The coordinator’s preferred writing style
B. The exact file path, function name, observed failure, and any tests already known to cover the behavior
C. A warning that the subagent should not disappoint the team
D. The names of unrelated modules in the same repository

**Answer:** B
**Explanation:** Concrete implementation context and validation information help the subagent act without needing follow-up. Stylistic and motivational details do not resolve missing technical context.

### Q13.
Why should a coordinator include both findings and raw structured evidence when possible?

A. Because the subagent can use the findings for speed and the evidence for verification or deeper analysis
B. Because prompts are graded by how much data they contain, regardless of relevance
C. Because raw evidence makes completion criteria unnecessary
D. Because findings alone are never useful

**Answer:** A
**Explanation:** A strong prompt balances curated conclusions with the underlying data that supports or refines them. Relevance still matters, and completion criteria remain necessary.

### Q14.
A subagent prompt says, "Continue from where I left off," and includes a log excerpt but no summary of prior reasoning. Why is this weak?

A. Logs are forbidden in subagent prompts
B. Raw artifacts alone may not communicate which parts were already analyzed, what conclusions were reached, or what remains unresolved
C. Prior reasoning should always be omitted to avoid bias
D. The prompt should focus on tone before content

**Answer:** B
**Explanation:** Prompt completeness requires enough synthesized state to orient the subagent, not just raw inputs. Without prior reasoning or status, the subagent may duplicate work or miss the intended target.

### Q15.
You are evaluating a proposed subagent handoff rubric. Which criterion best reflects this objective?

A. The prompt is short enough to fit on one screen
B. The prompt includes task goal, relevant findings, structured inputs, source metadata, known exclusions, and expected output
C. The prompt always instructs the subagent to ask questions before acting
D. The prompt avoids mentioning any earlier investigation

**Answer:** B
**Explanation:** This criterion captures the elements needed for autonomous task completion without returning for missing context. Brevity alone is not sufficient, and mandatory clarification defeats the objective.

---

[← Back to objectives index](README.md) · [Back to main index](../../README.md)
