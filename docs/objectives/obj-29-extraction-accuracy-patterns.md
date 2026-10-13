# Objective 29: Extraction accuracy patterns

[← Back to objectives index](README.md) · [Back to main index](../../README.md)

> **Exam objective:** Apply extraction accuracy patterns—structured schemas with optional fields, format normalization instructions, and few-shot examples—to reduce hallucination and improve consistency across varied document formats.

---

### Q1.
A team extracts dates from vendor forms, but outputs vary between `03/04/26`, `2026-03-04`, and `March 4th, 2026`. What is the best prompt design improvement?

A. Ask the model to keep the original date formatting for authenticity
B. Add explicit normalization instructions, such as returning dates in ISO 8601 format
C. Increase temperature so the model picks one format creatively
D. Remove the date field from the schema

**Answer:** B
**Explanation:** Normalization instructions reduce output variability and make downstream processing predictable. Keeping source formatting may preserve fidelity in some workflows, but it does not meet the consistency goal described.

### Q2.
A résumé extractor works well on corporate CVs but hallucinates graduation years on sparse one-page resumes. Which combination best addresses this?

A. Use optional fields in the schema and provide few-shot examples that leave education subfields empty or null when unsupported
B. Require all education fields so the model learns completeness
C. Ask for a confidence score only
D. Convert the entire task to free-form summarization

**Answer:** A
**Explanation:** Optional fields prevent fabrication when evidence is missing, and few-shot examples teach the model what abstention should look like in low-information cases. Requiring every field encourages hallucination.

### Q3.
A contract extractor must return payment terms as an integer number of days, even though documents express them as `Net 30`, `Due within thirty days`, or `Payment upon receipt`. What is the most effective pattern?

A. Leave the field as free text and normalize later manually
B. Add schema constraints plus normalization instructions and few-shot examples covering multiple phrasing patterns
C. Force the model to output the first number it sees
D. Remove the field because wording varies

**Answer:** B
**Explanation:** This combines structural guidance, transformation rules, and examples of varied source phrasing, which is exactly the pattern for consistent extraction across formats. Merely taking the first number would fail on phrases like `upon receipt`.

### Q4.
You are extracting phone numbers from global customer forms. Some forms include spaces, punctuation, or country codes. What instruction most improves consistency?

A. Return the number exactly as written, no matter the downstream need
B. Normalize to a documented target format, such as E.164 when enough information exists, otherwise leave null or preserve raw value in a separate field
C. Convert all numbers to U.S. local format
D. Strip country codes because they are inconsistent

**Answer:** B
**Explanation:** A target normalization standard improves consistency, but the design must still handle incomplete data honestly. Forcing a local format or discarding country codes would distort real values.

### Q5.
A few-shot example set shows only highly structured invoices with clearly labeled totals. The model performs poorly on narrative receipts. What is the best improvement?

A. Remove examples entirely so the model generalizes freely
B. Add representative few-shot examples spanning the messy formats seen in production
C. Increase max_tokens to make the model read more carefully
D. Ask the model to ignore labels

**Answer:** B
**Explanation:** Few-shot examples are most useful when they resemble the diversity of actual inputs. A narrow example set can overfit the model to idealized patterns and hurt performance on messy documents.

### Q6.
A schema has `state_province: string` required for all addresses, but many international records do not use that concept. Which accuracy pattern is best?

A. Make the field optional or nullable and clarify when it should be absent
B. Map missing regions to the city name
C. Require `N/A` as a literal output
D. Delete the entire address object

**Answer:** A
**Explanation:** Optionality aligned to real-world variation reduces hallucination and prevents invalid filler values. Mapping unrelated fields or sentinel strings degrades extraction quality.

### Q7.
An AP extraction workflow needs currency amounts normalized as decimals without symbols. Which prompt addition is most helpful?

A. "Be accurate"
B. "Return monetary amounts as numeric decimal values without currency symbols or commas; place currency code in its own field"
C. "Use whatever money format appears most often"
D. "Prefer readable formatting for analysts"

**Answer:** B
**Explanation:** Specific normalization instructions outperform vague guidance. Separating amount from currency code also preserves structure and avoids mixed-format outputs.

### Q8.
A bank onboarding extractor must parse `yes/no` answers from forms that sometimes say `Y`, `Checked`, `Selected`, or contain an `X` in a box. What pattern best improves consistency?

A. Use a boolean schema field and provide few-shot examples demonstrating how different marks map to true/false
B. Store the raw OCR text only
C. Ask the model to describe the checkbox artistically
D. Use a required string field with no examples

**Answer:** A
**Explanation:** Booleans provide the right target type, and examples across multiple source patterns teach the model how to interpret nonstandard markings consistently. Raw text alone leaves the normalization problem unsolved.

### Q9.
Why do few-shot examples often reduce hallucination in extraction tasks?

A. They eliminate the need for a schema
B. They demonstrate desired abstention behavior, formatting, and field interpretation on realistic inputs
C. They make the model deterministic in every case
D. They increase OCR accuracy directly

**Answer:** B
**Explanation:** Few-shot examples show the model how to behave, especially when evidence is partial or ambiguous. They do not replace schemas or guarantee determinism, but they strongly improve consistency.

### Q10.
A healthcare extractor processes intake forms from different clinics. Some use `DOB`, some `Birth Date`, and some `Date of Birth`. Which change most directly improves robust extraction?

A. Add a few-shot set covering alternate labels and keep a normalized target schema
B. Require users to submit only one approved form template
C. Instruct the model to ignore headings
D. Replace structured extraction with summarization

**Answer:** A
**Explanation:** Varied labels across document formats are exactly where representative examples help. The schema keeps the target consistent while the examples teach equivalence among source expressions.

### Q11.
A model extracts addresses but sometimes combines `address_line_2` into `address_line_1`, especially for apartment numbers. Which improvement is best?

A. Add field-level descriptions and examples showing how suites, apartments, and building names should be split
B. Delete `address_line_2`
C. Increase temperature to encourage diversity
D. Change both fields to booleans

**Answer:** A
**Explanation:** Fine-grained field guidance plus examples helps the model learn the intended segmentation. Removing fields or changing types avoids the problem by losing necessary structure.

### Q12.
A claims extractor must work across emailed PDFs, portal screenshots, and OCR text dumps. What is the strongest overall design approach?

A. Use a structured schema with optional fields, explicit normalization rules, and examples drawn from each source format
B. Use one long prose prompt with no schema so the model can adapt freely
C. Train separate human operators for each format instead of improving the prompt
D. Only process the clearest PDFs

**Answer:** A
**Explanation:** The objective specifically emphasizes combining schema design, normalization, and representative examples to handle format variation. This layered approach is more robust than relying on free-form adaptability alone.

### Q13.
A model extracts U.S. state codes, but source documents sometimes spell out full state names. What is the best instruction?

A. "Return any state information you see"
B. "Normalize U.S. states to their two-letter postal abbreviations; if the location is outside the U.S. or unclear, follow the schema's null/optional behavior"
C. "Prefer the longest version of the state name"
D. "Ignore state values unless they are already abbreviated"

**Answer:** B
**Explanation:** This instruction defines both the normalization target and the abstention behavior for unsupported cases. Vague or selective rules lead to inconsistent handling of legitimate inputs.

### Q14.
Your extractor returns good structured data on average, but analysts notice inconsistent capitalization and spacing in normalized outputs. Which change is most likely to help?

A. Add explicit formatting normalization instructions and examples that demonstrate exact expected output style
B. Remove the schema because it is too restrictive
C. Tell analysts to post-process everything by hand
D. Ask the model to be "cleaner"

**Answer:** A
**Explanation:** Exact formatting instructions plus examples reduce small but operationally important inconsistencies. Vague wording like "cleaner" rarely produces dependable standardization.

### Q15.
A team wants to improve extraction from heterogeneous tax forms. Which proposal best reflects the recommended accuracy pattern?

A. Add a schema with optional fields, specify normalized output formats, and include few-shot examples for both complete and incomplete forms
B. Keep the current free-form prompt and increase temperature for flexibility
C. Force every field to be present so the output shape never varies
D. Ask the model to explain its reasoning in detail instead of returning structured data

**Answer:** A
**Explanation:** This combines all three core accuracy patterns named in the objective: structured schemas, normalization instructions, and few-shot examples. The alternatives either increase hallucination risk or move away from structured extraction.

---

[← Back to objectives index](README.md) · [Back to main index](../../README.md)
