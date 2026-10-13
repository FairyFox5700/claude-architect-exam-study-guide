# Objective 25: Structured Output Method

[← Back to objectives index](README.md) · [Back to main index](../../README.md)

> **Exam objective:** Select and implement the most reliable structured output method—tool use with JSON schema, prompt-based formatting, or prefilled responses—based on required schema compliance strictness.

---

### Q1.
You are building a workflow where model output must always populate a downstream system expecting exact JSON keys, types, and required fields. Which method is most reliable?

A. Prompt-based formatting alone  
B. Tool use with a JSON schema  
C. Free-form natural language with examples  
D. Prefilled prose paragraphs

**Answer:** B  
**Explanation:** When strict schema compliance is required, tool use with a JSON schema provides the strongest structural guarantee. Prompt-only formatting is less reliable because the model can drift from exact syntax or required fields.

### Q2.
A prototype internal dashboard needs lightweight structured output, but occasional formatting cleanup in application code is acceptable. Which method is usually sufficient?

A. Tool use with schema is always mandatory  
B. Prompt-based formatting can be appropriate when strict compliance is not critical  
C. Prefilled responses are the only option  
D. Avoid structure entirely

**Answer:** B  
**Explanation:** Prompt-based formatting is often acceptable for lower-stakes scenarios where some post-processing tolerance exists. It is less strict than schema-backed tool use but simpler for lightweight needs.

### Q3.
You want the model to answer with one of three exact labels: APPROVE, REJECT, or ESCALATE. Which method is often a good fit?

A. Prefilled response starting the answer in the required form  
B. A long essay prompt  
C. Random sampling of outputs  
D. No constraints because the labels are obvious

**Answer:** A  
**Explanation:** Prefilled responses are useful when the desired output shape is very constrained and small, such as fixed labels or a known prefix. A full JSON schema would also work, but prefill is a simple strong pattern for tightly bounded outputs.

### Q4.
Which scenario most strongly argues against relying only on prompt-based formatting?

A. The output is displayed directly to a human who can interpret minor variations  
B. Downstream automation breaks if one required JSON field is missing or a type is wrong  
C. The response is short  
D. The user prefers concise answers

**Answer:** B  
**Explanation:** If a single structural deviation can break downstream automation, you need stronger guarantees than prompt wording alone. Schema-backed tool use is the safer design in that case.

### Q5.
A model must extract invoice data into a validated object with fields for vendor, invoice_number, due_date, and total_amount. Some fields are required and must have the correct types. What is the best implementation choice?

A. Ask for a markdown table  
B. Use tool use with a JSON schema defining required properties and types  
C. Ask the model to "be careful with formatting"  
D. Return plain English and parse it later with regexes only

**Answer:** B  
**Explanation:** Required properties and type constraints point directly to schema-backed tool use. Tables and free-form text are weaker contracts and increase downstream parsing risk.

### Q6.
You need a yes/no classifier result embedded inside a short templated sentence sent to a human reviewer. Which method may be most practical?

A. Tool use with a deeply nested JSON schema  
B. Prefilled response or prompt-shaped formatting to constrain the short template  
C. No structure, just a paragraph  
D. Message Batches API only

**Answer:** B  
**Explanation:** For a tiny, human-facing response with limited variants, prefill or simple prompt formatting can be practical and sufficient. A full schema may be unnecessarily heavy if machine validation is not the primary need.

### Q7.
An engineer says, "Prompt-based formatting is enough for all structured outputs." What is the best rebuttal?

A. Correct; schemas are never needed  
B. It depends on strictness requirements—prompting may be fine for soft structure, but strict machine-consumable outputs usually need schema-backed tool use  
C. Prompting only works for long responses  
D. Structured outputs are impossible with model APIs

**Answer:** B  
**Explanation:** The right method depends on how costly deviations are. Soft structure can tolerate prompt-based formatting, while strict integrations generally require stronger enforcement mechanisms.

### Q8.
Which requirement is the clearest signal to choose tool use with JSON schema?

A. The output must be entertaining  
B. The output will be read once by a human and discarded  
C. The output must conform to an exact schema for automated downstream processing  
D. The prompt is under 100 tokens

**Answer:** C  
**Explanation:** Exact machine-consumable schema conformance is the strongest reason to use schema-backed tool calls. Human-only consumption and stylistic preferences do not create the same strictness requirement.

### Q9.
You need the model to emit a two-field object most of the time, but occasional malformed JSON is acceptable because a retry layer can recover. Which method might be acceptable if simplicity is prioritized?

A. Prompt-based formatting  
B. Only natural-language paragraphs  
C. A screenshot-based workflow  
D. Eliminate validation entirely

**Answer:** A  
**Explanation:** If the application can tolerate occasional reformatting failures and has recovery logic, prompt-based formatting may be an acceptable trade-off. The key is that strict compliance is not mandatory on every first attempt.

### Q10.
What is the main advantage of prefilled responses compared with fully unconstrained prompting?

A. They nudge the model into a desired output shape by starting the structure for it  
B. They validate types automatically  
C. They eliminate the need for application logic  
D. They always outperform schemas

**Answer:** A  
**Explanation:** Prefill works by biasing completion toward a known structure or label space. It is a shaping technique, not a full validation mechanism like a schema.

### Q11.
A regulator requires every generated decision object to include `decision`, `justification_code`, and `review_required` with exact boolean and enum constraints. Which method best satisfies the requirement?

A. Prompt-based formatting with an example  
B. Tool use with JSON schema enforcing required fields and allowed values  
C. Prefilled natural language sentence  
D. Any method because the model usually follows instructions

**Answer:** B  
**Explanation:** Regulatory constraints and exact field/value requirements call for the most reliable structured-output mechanism available. Schema-backed tool use provides explicit enforcement of required fields and allowed types or enums.

### Q12.
Which use case is the best match for prefilled responses rather than a full schema?

A. Returning a complex nested purchase-order object for direct database insertion  
B. Producing one of several fixed triage labels at the start of the answer  
C. Emitting a validated numeric array with range constraints  
D. Writing a machine-checked audit record with required nested objects

**Answer:** B  
**Explanation:** Prefill excels when the output space is small and shape-constrained, such as fixed labels or templated short responses. Complex validated objects are better handled with schema-backed tool use.

### Q13.
Why is prompt-based formatting considered less reliable than schema-backed tool use for strict outputs?

A. It prevents the model from producing JSON at all  
B. The model may omit fields, change key names, or introduce formatting drift despite instructions  
C. It only works in batch mode  
D. It requires too many tokens to ever be practical

**Answer:** B  
**Explanation:** Prompt-only structure relies on instruction following rather than explicit structural enforcement. Even good models can occasionally drift in key names, punctuation, or required fields under prompt-only control.

### Q14.
You are designing an extraction system with three tiers: strict production integrations, semi-structured analyst tools, and fixed-label approvals. Which mapping is best?

A. Prompt formatting for strict integrations, free text for analyst tools, and schemas for fixed labels  
B. Schema-backed tool use for strict integrations, prompt formatting for semi-structured analyst tools, and prefilled responses for fixed-label approvals  
C. Prefill for everything  
D. Schema-backed tool use only for human-readable summaries

**Answer:** B  
**Explanation:** This mapping aligns method strength to output strictness. Strict integrations need schemas, analyst tools often tolerate softer structure, and fixed-label tasks are well served by prefill patterns.

### Q15.
Which statement best summarizes how to choose among tool use with schema, prompt formatting, and prefilled responses?

A. Always use the simplest method regardless of failure cost  
B. Choose based on required schema compliance strictness and how costly output deviation is for the downstream workflow  
C. Use prefilled responses only for long essays  
D. Structured output choices are unrelated to system design

**Answer:** B  
**Explanation:** Output-method selection should be driven by strictness requirements and the operational cost of malformed output. Stronger guarantees justify stronger mechanisms, while lighter-weight methods are fine when deviation is tolerable.

---

[← Back to objectives index](README.md) · [Back to main index](../../README.md)
