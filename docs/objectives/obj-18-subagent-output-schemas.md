# Objective 18: Subagent Output Schemas

[← Back to objectives index](README.md) · [Back to main index](../../README.md)

> **Exam objective:** Design subagent output schemas that render structured data, prose summaries, and citation metadata in the format best suited to downstream synthesis and reporting.

---

### Q1.
You are designing a research subagent whose results will be merged into a final comparative report. Downstream consumers need both a short narrative and machine-readable fields such as product name, version, and evidence URL. Which output design is best?

A. Free-form prose only  
B. A rigid table with no explanatory text  
C. A hybrid schema with structured fields plus a prose summary and citations  
D. Screenshots instead of text  

**Answer:** C  
**Explanation:** A hybrid schema supports both automation and human synthesis. Pure prose is hard to aggregate, pure tables lose nuance, and screenshots are poor inputs for downstream reasoning.

### Q2.
Why should citation metadata typically be a distinct part of a subagent output schema rather than embedded inconsistently inside prose?

A. Separate citations let downstream synthesis reliably trace claims back to sources  
B. Embedded citations are always invalid markdown  
C. Distinct citations reduce token usage to zero  
D. Separate citations eliminate the need for summaries  

**Answer:** A  
**Explanation:** Explicit citation fields make provenance dependable and easy to parse. Prose may still mention sources, but inconsistent embedding makes aggregation and validation harder.

### Q3.
A parent agent must combine findings from ten file-analysis subagents and produce a defect report. Which schema feature is most important for each subagent to include?

A. Personal writing style preferences  
B. Stable fields for severity, finding summary, location, and evidence  
C. A full copy of every file read  
D. Source code formatting opinions  

**Answer:** B  
**Explanation:** Consistent structured fields enable the parent to sort, deduplicate, and synthesize findings accurately. Full file dumps and stylistic commentary create noise without helping downstream reporting.

### Q4.
When is prose-only output from a subagent most likely to be insufficient?

A. When the result will be read only once by a human  
B. When the result must be aggregated, filtered, or transformed by another agent  
C. When the task is very small  
D. When the subagent read only one source  

**Answer:** B  
**Explanation:** Downstream synthesis benefits from predictable fields that can be compared across outputs. Prose-only responses are harder to normalize, deduplicate, or rank when many results must be merged.

### Q5.
You want a subagent to report both extracted metrics and an overall judgment of system health. Which schema design best supports that?

A. A list of raw numbers only  
B. A single sentence saying the system is fine  
C. Separate sections for structured metrics, summary assessment, and evidence  
D. A binary healthy/unhealthy flag with no context  

**Answer:** C  
**Explanation:** Structured metrics capture the facts, while a narrative assessment explains their significance and citations anchor both to evidence. Simpler formats lose either interpretability or analytical precision.

### Q6.
Which schema choice most improves interoperability when multiple subagents contribute to the same parent workflow?

A. Let each subagent invent its own headings to maximize flexibility  
B. Use a shared schema with defined field names and optional extension fields  
C. Require only paragraph text so formats do not conflict  
D. Omit citations to keep outputs short  

**Answer:** B  
**Explanation:** Standardization makes synthesis predictable while optional fields preserve flexibility for task-specific details. Fully custom formats shift unnecessary complexity to the parent agent.

### Q7.
A subagent is tasked with scanning policy documents for compliance statements. The parent needs to know whether a claim is directly quoted or inferred. What is the best schema addition?

A. A "confidence" field only  
B. A "source_type" or "evidence_mode" field distinguishing quoted vs inferred evidence  
C. Longer prose paragraphs  
D. A screenshot attachment requirement  

**Answer:** B  
**Explanation:** Confidence alone does not distinguish direct textual support from inference. A dedicated field capturing evidence mode makes the final synthesis more transparent and accurate.

### Q8.
What is the main advantage of including both a concise summary field and a longer notes field in a subagent schema?

A. It guarantees the parent will never need to read citations  
B. It supports quick scanning while preserving richer nuance when needed  
C. It doubles the result count for reporting  
D. It replaces the need for structured fields  

**Answer:** B  
**Explanation:** A short summary helps ranking and triage, while a longer notes field preserves caveats and details. This layered design helps both human readers and downstream agents operate efficiently.

### Q9.
You are designing outputs for a subagent that reviews several URLs and may find no relevant evidence on some of them. What is the best schema behavior?

A. Omit URLs with no findings so the parent assumes they were never checked  
B. Include a checked_sources section showing searched items and result status  
C. Fabricate a neutral summary for each missing source  
D. Return only successful findings because negative evidence is useless  

**Answer:** B  
**Explanation:** Recording which sources were checked prevents ambiguity and supports auditability. Negative or null results often matter because they narrow uncertainty and document search coverage.

### Q10.
Which design best supports a parent agent that must rank findings by actionability?

A. A schema with fields for impact, confidence, and recommended next step  
B. A schema that contains only source URLs  
C. A schema that prohibits interpretation  
D. A schema that uses different terms for priority in every run  

**Answer:** A  
**Explanation:** Ranking actionability requires both evidence strength and practical consequence, plus a suggested follow-up. URLs alone are insufficient, and inconsistent terminology breaks comparability across results.

### Q11.
In which situation is a plain markdown table a poor sole output format?

A. When every result is a short numeric measurement  
B. When entries need nested citations, caveats, and multi-paragraph reasoning  
C. When the parent only needs two columns  
D. When results will never be summarized  

**Answer:** B  
**Explanation:** Tables are useful for compact regular fields, but they become awkward when each item needs nuanced explanations and multiple evidence references. A richer schema handles both structure and prose more effectively.

### Q12.
You want downstream synthesis to quote a subagent's exact supporting text snippet. Which schema field is most valuable?

A. citation_excerpt  
B. model_temperature  
C. paragraph_count  
D. report_theme_color  

**Answer:** A  
**Explanation:** A citation excerpt preserves the exact evidence fragment needed for precise quoting and verification. The other fields do not help with traceable claim support.

### Q13.
Why is it useful to distinguish "facts" from "interpretation" in a subagent report schema?

A. It allows the parent to preserve evidence separately from analytical judgment during synthesis  
B. It prevents the subagent from making any conclusions  
C. It guarantees all interpretations are correct  
D. It removes the need for citations  

**Answer:** A  
**Explanation:** Separating observations from conclusions helps the parent decide how strongly to state the result and makes conflicting interpretations easier to compare. It does not eliminate judgment; it makes that judgment more transparent.

### Q14.
What is the best reason to include a schema version or stable heading conventions in subagent outputs used over time?

A. It lets downstream consumers evolve parsing logic safely as formats change  
B. It makes the output look more formal  
C. It guarantees backward compatibility forever  
D. It is only useful for binary files  

**Answer:** A  
**Explanation:** Versioning or stable conventions reduce brittleness when workflows evolve. They do not guarantee perfect compatibility, but they greatly improve maintainability for long-lived synthesis pipelines.

### Q15.
Which subagent output is best suited for downstream synthesis and reporting?

A. "Here are some thoughts" followed by several unstructured paragraphs  
B. A schema containing structured findings, an executive summary, citation metadata, and optional caveats  
C. A CSV with no explanations or evidence  
D. A list of URLs and nothing else  

**Answer:** B  
**Explanation:** The strongest design balances machine-readability, human readability, and provenance. Unstructured prose, raw CSVs, or bare URLs each omit key ingredients needed for reliable downstream synthesis.

---

[← Back to objectives index](README.md) · [Back to main index](../../README.md)
