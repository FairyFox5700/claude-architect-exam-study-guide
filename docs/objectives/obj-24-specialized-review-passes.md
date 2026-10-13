# Objective 24: Specialized Review Passes

[← Back to objectives index](README.md) · [Back to main index](../../README.md)

> **Exam objective:** Design specialized review passes that separate concerns—security, business logic, API design—into focused prompts with dedicated few-shot examples, preventing recall trade-offs from competing concerns in a single prompt.

---

### Q1.
A team asks one prompt to review code for SQL injection, broken business rules, REST API consistency, performance, and naming style. The results are shallow and inconsistent. What is the best redesign?

A. Make the single prompt even longer  
B. Split the review into specialized passes such as security, business logic, and API design with targeted examples  
C. Ask the model to "try harder" in the same prompt  
D. Remove examples so the model has more room

**Answer:** B  
**Explanation:** Specialized passes reduce competing objectives and let each prompt focus on one evaluation lens. Dedicated few-shot examples also calibrate the model toward the specific defect class each pass should detect.

### Q2.
Why can a single omnibus review prompt reduce recall for important issues?

A. Models cannot read more than one instruction  
B. Competing concerns dilute attention and create trade-offs in what the model surfaces  
C. Few-shot examples always lower accuracy  
D. API design and security are logically identical

**Answer:** B  
**Explanation:** When many review goals are mixed together, the model may under-attend to some of them or return generic feedback. Separating concerns reduces competition for prompt space and retrieval focus.

### Q3.
A security pass should focus on authentication flaws, injection risks, and secret exposure. Which few-shot examples are most appropriate?

A. Examples of variable naming improvements  
B. Examples of pricing-rule miscalculations  
C. Examples showing vulnerable patterns and the specific high-confidence security findings expected  
D. Examples of UI wording changes

**Answer:** C  
**Explanation:** Few-shot examples should match the target review concern closely. Security-oriented exemplars help the model learn what to flag and what level of evidence is expected in that pass.

### Q4.
You need to review a new endpoint implementation. Which sequence best aligns with specialized review-pass design?

A. One pass for everything, then no further analysis  
B. Separate passes for security, business logic correctness, and API contract quality  
C. A style pass only  
D. A random selection of three concerns each run

**Answer:** B  
**Explanation:** The objective calls for deliberate concern separation into focused prompts, not random or single-shot all-in-one review. Endpoints naturally benefit from distinct security, correctness, and API-design lenses.

### Q5.
An engineering manager says, "Why not just ask for security and business logic in the same prompt? They're both important." What is the best reply?

A. They should always be combined to save tokens  
B. Combining them can cause the model to miss issues because the concerns compete for attention and example budget  
C. Security should replace business logic entirely  
D. Few-shot examples are irrelevant either way

**Answer:** B  
**Explanation:** Importance alone does not mean concerns should share one prompt. When each defect class needs different cues and examples, separate passes often improve coverage and diagnostic precision.

### Q6.
Which outcome most strongly indicates that specialized passes are working better than a monolithic review prompt?

A. The model writes longer responses  
B. Findings become more focused, with higher relevance to each concern and fewer generic comments  
C. The code compiles faster  
D. The prompts are shorter than before

**Answer:** B  
**Explanation:** Success is reflected in better issue detection quality and clearer categorization, not merely response length or compilation behavior. Focused prompts should produce sharper, more concern-specific findings.

### Q7.
You are designing a business-logic review pass for an order-discount engine. Which instruction set is most appropriate?

A. "Find any issue of any kind in this repository."  
B. "Evaluate whether discount eligibility, stacking rules, rounding, and approval thresholds match the stated policy examples."  
C. "Check for SQL injection only."  
D. "Rewrite the code in another language."

**Answer:** B  
**Explanation:** A business-logic pass should be anchored in policy behavior and domain rules, not generic issue hunting. The instruction is narrowly scoped to the logic class the pass is intended to validate.

### Q8.
An API-design review pass is producing security findings instead of contract-quality feedback. What is the best adjustment?

A. Add more unrelated concerns to make the model broader  
B. Refine the pass prompt and few-shot examples so they emphasize versioning, status codes, schema consistency, and backward compatibility  
C. Disable all examples  
D. Replace the pass with random sampling

**Answer:** B  
**Explanation:** If a pass drifts into the wrong concern, the fix is tighter scope and better-aligned exemplars. Focused examples teach the model what belongs in that pass and what does not.

### Q9.
Which review item is best suited for a security-focused pass rather than a business-logic pass?

A. A discount applies twice when policy allows it only once  
B. An endpoint accepts user-controlled SQL fragments in a filter parameter  
C. A response uses 200 instead of 201 on resource creation  
D. A tax rule uses the wrong jurisdiction threshold

**Answer:** B  
**Explanation:** User-controlled SQL fragments are a classic security issue. The other options concern business behavior or API semantics and would be better caught in different specialized passes.

### Q10.
Why are dedicated few-shot examples especially valuable in specialized review passes?

A. They guarantee zero false positives  
B. They calibrate the model on the defect patterns, evidence threshold, and response style expected for that specific concern  
C. They remove the need for clear instructions  
D. They are only useful for translation tasks

**Answer:** B  
**Explanation:** Few-shot examples teach the model what "good review behavior" looks like for a narrowly scoped task. They do not guarantee perfection, but they improve consistency and relevance within the pass.

### Q11.
A team reviews payment code with three passes: security, business logic, and API design. The security pass flags PCI exposure, the logic pass catches refund calculation errors, and the API pass detects inconsistent idempotency semantics. What does this most clearly demonstrate?

A. Specialized passes can surface different classes of issues that a single prompt may underemphasize  
B. One of the three passes is unnecessary  
C. API design and business logic are the same concern  
D. Few-shot examples should now be removed

**Answer:** A  
**Explanation:** The example shows each focused pass discovering issues aligned to its own lens, illustrating the practical value of separation. This is exactly the outcome specialized review architectures aim to produce.

### Q12.
Which prompt is the strongest example of a specialized API-design pass?

A. "Review for security vulnerabilities, pricing errors, and code style."  
B. "Assess whether endpoint naming, status codes, pagination, error schemas, and backward compatibility follow our API conventions. Ignore business-rule correctness unless it affects the contract."  
C. "Summarize the repository."  
D. "Find bugs and be creative."

**Answer:** B  
**Explanation:** This prompt is sharply scoped to API contract quality and explicitly excludes unrelated concerns except where they intersect with the contract. That discipline is central to specialized passes.

### Q13.
What is the primary risk of stuffing too many few-shot examples for unrelated concerns into one review prompt?

A. The model becomes multilingual  
B. Relevant patterns for each concern compete for limited prompt attention and can reduce recall  
C. The API stops accepting requests  
D. The examples automatically become incorrect

**Answer:** B  
**Explanation:** Prompt space and attention are finite, so unrelated examples can crowd out the cues needed for any one concern. Focused exemplar sets are more effective than mixed, heterogeneous ones.

### Q14.
You have budget for only one additional pass after a general bug review. The code handles customer authentication and authorization. Which specialized pass is most justified?

A. Brand voice review  
B. Security review pass with auth-specific few-shot examples  
C. Comment formatting review  
D. Color accessibility review

**Answer:** B  
**Explanation:** Authentication and authorization code has elevated security risk, so a security-focused pass is the highest-value specialization. Auth-specific examples further tune the model toward likely defect patterns.

### Q15.
Which design best aligns with the objective when reviewing a complex pull request?

A. One giant prompt covering every concern with a mixed set of examples  
B. Several focused passes, each with scoped instructions and examples tailored to that concern  
C. No prompt instructions, only raw code  
D. A single pass followed by random reviewer guesses

**Answer:** B  
**Explanation:** The objective explicitly favors separate concern-specific passes with dedicated few-shot examples. This structure minimizes recall trade-offs and improves the reliability of findings within each category.

---

[← Back to objectives index](README.md) · [Back to main index](../../README.md)
