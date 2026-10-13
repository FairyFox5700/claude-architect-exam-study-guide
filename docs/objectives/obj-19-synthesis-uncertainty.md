# Objective 19: Synthesis & Uncertainty

[← Back to objectives index](README.md) · [Back to main index](../../README.md)

> **Exam objective:** Design synthesis agent behavior that preserves source-level uncertainty, distinguishing well-established findings from contested claims rather than collapsing conflicting data into single confident statements.

---

### Q1.
Two subagents review different source documents. One says a feature is generally available, while the other cites a newer source calling it preview-only in one region. What should the synthesis agent do?

A. Pick the more optimistic answer so the report is actionable  
B. State that availability is uncertain, describe the conflict, and cite both sources  
C. Average the claims and say the feature is "partially GA"  
D. Omit the topic to avoid confusion  

**Answer:** B  
**Explanation:** Good synthesis preserves the disagreement and anchors it to the underlying evidence. Collapsing conflicting claims into a single confident statement would misrepresent the source record.

### Q2.
Why is preserving source-level uncertainty important in multi-source reporting?

A. It makes the report longer  
B. It helps downstream decisions reflect the actual strength and consistency of evidence  
C. It avoids the need for citations  
D. It guarantees consensus later  

**Answer:** B  
**Explanation:** Decision-makers need to know not just what was found, but how stable or contested those findings are. Treating weak or conflicting evidence as settled can lead to overconfident and incorrect conclusions.

### Q3.
A synthesis agent sees nine sources supporting one interpretation and one source contradicting them with unclear provenance. What is the best output?

A. Declare both views equally likely  
B. Ignore the contradictory source completely  
C. Present the majority-supported conclusion as well-established while noting the weaker conflicting source and its limitations  
D. Report only the contradiction because it is more surprising  

**Answer:** C  
**Explanation:** Preserving uncertainty does not mean flattening all evidence into false equivalence. The synthesis should reflect evidentiary weight while still documenting material conflicts.

### Q4.
Which wording best reflects uncertainty-aware synthesis?

A. "The system definitely encrypts every backup."  
B. "Sources indicate backups are encrypted in the managed service path, but one older document suggests exceptions for legacy exports."  
C. "Encryption is probably fine."  
D. "No one knows whether backups are encrypted."  

**Answer:** B  
**Explanation:** This wording communicates the leading conclusion, scope, and the specific source of uncertainty. The other choices are either overconfident, too vague, or overly dismissive.

### Q5.
What is the best way to handle a claim that is supported only by one tertiary source with no primary citation?

A. Present it as established fact if it fits the narrative  
B. Exclude it from the report entirely  
C. Label it as weakly supported or unverified and cite the limited basis  
D. Rewrite it as a confident summary to reduce noise  

**Answer:** C  
**Explanation:** Weak evidence can still be useful if clearly labeled as such. The key is to preserve the limited support instead of overstating certainty or silently discarding potentially relevant information.

### Q6.
When several sources use different terminology that may or may not describe the same concept, what should the synthesis agent do?

A. Assume they are identical and merge them into one statement  
B. Note the possible mapping, explain the ambiguity, and avoid stronger normalization than the sources justify  
C. Prefer whichever term appears first chronologically  
D. Replace all terms with a new invented category  

**Answer:** B  
**Explanation:** Uncertainty can arise from terminology mismatch as well as factual disagreement. The synthesis agent should clarify the possible equivalence without pretending the mapping is confirmed if it is not.

### Q7.
Which report structure best supports preservation of uncertainty?

A. Findings grouped into confirmed, likely, and contested sections with citations  
B. A single bullet list of conclusions without qualifiers  
C. Only an executive summary  
D. A numeric average of all claims  

**Answer:** A  
**Explanation:** Explicit confidence or certainty bands help readers distinguish solid conclusions from weaker or disputed ones. Unqualified lists hide evidentiary variation and can mislead downstream consumers.

### Q8.
A parent agent asks for "the answer" even though the evidence is split and unresolved. What is the best synthesis response?

A. Provide one answer anyway because decisiveness is always preferred  
B. State the leading interpretation if one exists, but clearly mark remaining uncertainty and the reasons it persists  
C. Refuse to summarize at all  
D. Randomly choose the most recent source  

**Answer:** B  
**Explanation:** Synthesis should still be useful, but usefulness comes from calibrated judgment, not false certainty. The agent can provide the best-supported view while being explicit about unresolved conflicts.

### Q9.
What is a key risk of collapsing conflicting data into a single polished conclusion?

A. The result may hide important disagreement and overstate confidence  
B. The report becomes too short  
C. Citations become easier to manage  
D. The parent agent saves tokens  

**Answer:** A  
**Explanation:** Over-compression can erase nuance that materially affects the correctness or trustworthiness of the final answer. Token savings are not worth distorting the evidence base.

### Q10.
How should a synthesis agent treat a source that is newer but less authoritative than an older primary document?

A. Always prefer the newer source  
B. Always prefer the older source  
C. Evaluate both recency and authority, and describe the tension if it affects confidence  
D. Ignore timestamps and authority completely  

**Answer:** C  
**Explanation:** Source quality is multi-dimensional; neither recency nor authority alone always settles the matter. A good synthesis explains why uncertainty remains when these factors pull in different directions.

### Q11.
Which phrase most clearly signals a contested claim rather than a settled one?

A. "It is proven that..."  
B. "Evidence is mixed: operational docs say X, while release notes suggest Y."  
C. "Everyone agrees that..."  
D. "This must be true."  

**Answer:** B  
**Explanation:** The phrase explicitly marks disagreement and identifies the competing evidence classes. The other options imply confidence unsupported by the scenario.

### Q12.
If one subagent reports a confident conclusion but provides thin evidence, how should the synthesis agent respond?

A. Preserve the confidence level exactly as given  
B. Recalibrate confidence based on the actual evidence and state that the claim is less certain than the subagent wording suggests  
C. Delete the finding automatically  
D. Promote the finding because confidence is contagious across agents  

**Answer:** B  
**Explanation:** Synthesis is not mere repetition; it is evidence-weighted integration. The parent should evaluate the support behind a claim and avoid inheriting unwarranted certainty from upstream phrasing.

### Q13.
What is the best practice when no source fully resolves a disputed point?

A. Invent a compromise answer  
B. Declare that further investigation would be needed and specify what evidence would resolve the uncertainty  
C. Omit the dispute so the final report looks cleaner  
D. Choose whichever answer is simpler to explain  

**Answer:** B  
**Explanation:** A good uncertainty-aware synthesis not only marks unresolved questions but also clarifies how they might be resolved. This keeps the output actionable without overstating what is known.

### Q14.
Which scenario most strongly requires uncertainty-preserving synthesis?

A. Ten identical copies of the same primary specification all say the same thing  
B. Multiple sources conflict on quota limits across regions and publication dates  
C. A single local config file defines a numeric timeout  
D. A test result clearly passes  

**Answer:** B  
**Explanation:** Conflicting multi-source claims are exactly where synthesis discipline matters most. The other situations involve little or no material ambiguity.

### Q15.
What is the best guiding principle for synthesis under uncertainty?

A. Prefer fluency over fidelity  
B. Preserve distinctions in evidence strength and disagreement instead of smoothing them away  
C. Never offer any conclusion when conflict exists  
D. Treat all sources as equally authoritative  

**Answer:** B  
**Explanation:** The synthesis agent's duty is to remain faithful to the evidence landscape, including disagreement and uneven support. That may still allow conclusions, but only with calibrated confidence and explicit caveats.

---

[← Back to objectives index](README.md) · [Back to main index](../../README.md)
