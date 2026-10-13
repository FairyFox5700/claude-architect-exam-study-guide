# Objective 26: Extraction schema design

[← Back to objectives index](README.md) · [Back to main index](../../README.md)

> **Exam objective:** Design extraction schemas with optional fields, nullable values, and appropriate enum definitions that allow the model to accurately represent missing or ambiguous information without fabricating values.

---

### Q1.
A team extracts invoice data from scanned PDFs. Some invoices include a purchase order number, while others do not. The current schema requires `purchase_order_number: string`, and the model often invents values like "N/A-001" when none is present. What is the best schema change?

A. Keep the field required and instruct the model to guess from surrounding text
B. Make `purchase_order_number` optional or nullable and explicitly allow omission when missing
C. Replace the field with a boolean `has_purchase_order`
D. Convert all missing values to the string `"UNKNOWN"`

**Answer:** B
**Explanation:** Optional or nullable fields let the model represent missing data honestly instead of fabricating placeholders. A required string encourages invented content, while a boolean loses the actual value and `"UNKNOWN"` mixes missingness with real data.

### Q2.
You are designing a schema for extracting a patient's smoking status from intake forms. Valid states are "current", "former", "never", and sometimes the form is illegible. Which design best preserves accuracy?

A. Use a free-form string so the model can explain any uncertainty
B. Use an enum for the known statuses plus a nullable field when status cannot be determined
C. Force one of the three known statuses because downstream systems require a value
D. Use a number from 1 to 3 and reserve 0 for unreadable

**Answer:** B
**Explanation:** An enum constrains valid classifications, and null supports cases where the source does not justify a classification. Free-form strings reduce consistency, while forcing a status or encoding values numerically hides uncertainty and increases error risk.

### Q3.
A contract extraction workflow captures `termination_notice_days`. Some agreements state "thirty (30) days," while others have no termination clause. Which schema is most appropriate?

A. `termination_notice_days: integer` required for every contract
B. `termination_notice_days: string` so any text can be copied verbatim
C. `termination_notice_days: integer | null` with instructions to return null when absent
D. `termination_notice_days: boolean` indicating whether a termination clause exists

**Answer:** C
**Explanation:** The normalized target is numeric days, but the clause may be absent, so nullable integer is the best representation. A required integer invites hallucination, a raw string weakens downstream use, and a boolean discards needed detail.

### Q4.
Your extraction schema includes a field `shipping_method` with enum values `air`, `ground`, and `sea`. New documents frequently say "courier," which is not semantically equivalent to any existing option. What should you do?

A. Map "courier" to `ground` because it is usually land-based
B. Add an `other` or similar enum strategy only if downstream can handle it, otherwise revisit the ontology before deployment
C. Tell the model to pick the closest enum value for compatibility
D. Keep the enum unchanged and require a best-effort guess

**Answer:** B
**Explanation:** Enums should reflect the real domain, not force lossy mappings. If common source values do not fit, the schema or ontology needs revision; guessing the closest value systematically corrupts data.

### Q5.
A lender wants to extract co-borrower information from applications. Many forms are for single applicants only. Which design best avoids fabricated co-borrower details?

A. Always require a `co_borrower` object with blank strings for missing subfields
B. Omit the `co_borrower` object entirely or allow it to be null when no co-borrower exists
C. Create a `co_borrower_name` string and set it to `"NONE"` when missing
D. Duplicate primary borrower data into the co-borrower fields when only one applicant is listed

**Answer:** B
**Explanation:** Optional or nullable nested objects cleanly represent absence and prevent the model from filling subfields with invented values. Blank strings, sentinel text, or copied primary data all create misleading records.

### Q6.
You extract `incident_severity` from support tickets using an enum: `sev1`, `sev2`, `sev3`, `sev4`. Many tickets contain no severity at all because they are untriaged. What is the best approach?

A. Default missing severity to `sev3` as a neutral midpoint
B. Expand the enum with `untriaged` only if it is a real business state; otherwise allow null
C. Infer severity from sentiment in the ticket description
D. Store the field as free text instead of an enum

**Answer:** B
**Explanation:** If `untriaged` is an authentic operational state, model it explicitly; if not, null correctly represents unknown or missing information. Defaulting or inferring severity fabricates data, and free text sacrifices consistency.

### Q7.
A schema includes `middle_name: string | null` for HR onboarding. Why is nullable preferable to requiring an empty string when the applicant has no middle name?

A. Null clearly distinguishes unknown or absent data from an intentionally provided empty value
B. Empty strings consume less storage than nulls
C. Null prevents the model from returning any other fields
D. Empty strings are invalid JSON in most APIs

**Answer:** A
**Explanation:** Null preserves semantics by separating absence from content. Empty strings are valid JSON but can blur whether the field was truly missing, normalized away, or incorrectly extracted.

### Q8.
You are extracting `court_decision` from legal summaries. Some documents contain conflicting references because they mention both a trial ruling and an appellate outcome. Which schema design best supports this ambiguity without forcing fabrication?

A. Single required string field containing the model's best guess
B. Enum with one required final value chosen by confidence
C. Nullable structured field plus optional `source_span` or notes field to capture unresolved ambiguity
D. Boolean field `decision_present`

**Answer:** C
**Explanation:** When the source is ambiguous or multi-layered, the schema should allow null and preserve evidence or notes rather than forcing a single fabricated conclusion. A single guess hides the ambiguity and weakens auditability.

### Q9.
A resume parser captures `certifications`. Some resumes have none, some have one, and some list many. Which representation is best?

A. Required string with comma-separated values
B. Nullable array of strings or an empty array when the section is clearly absent, depending on the chosen semantics
C. Single enum of the most common certifications
D. Boolean `has_certifications`

**Answer:** B
**Explanation:** Arrays fit repeated values, and the design can distinguish between no certifications and unknown extraction status using null versus empty array. Comma-separated strings and booleans lose structure, while a single enum cannot represent multiple certifications.

### Q10.
A bank statement extractor must classify account type as `checking`, `savings`, or `credit`. Some statements only show an account number and bank logo. What should the schema and prompt encourage?

A. Force the model to infer account type from transaction patterns
B. Use an enum for valid account types and allow null when the statement does not explicitly support classification
C. Replace the field with a free-form justification paragraph
D. Default all unrecognized statements to `checking`

**Answer:** B
**Explanation:** Enums constrain valid outputs while null prevents unsupported inference. Guessing from patterns or defaulting values creates false certainty, and free-form text does not satisfy structured extraction goals.

### Q11.
A property listing extractor has a field `hoa_fee_monthly_usd`. Some listings state "HOA varies" without a number. What is the best design?

A. Use integer and set 0 when no numeric fee is provided
B. Use string so `"varies"` can be returned directly in the amount field
C. Use nullable numeric fee plus a separate optional note/status field if business needs to capture non-numeric qualifiers
D. Convert `"varies"` to the market average fee

**Answer:** C
**Explanation:** The amount field should keep its numeric meaning, while a separate note or status field can preserve source nuance. Setting 0 or an average fabricates facts, and using string weakens numeric usability.

### Q12.
Why can overly broad enums harm extraction quality?

A. They always increase token usage beyond practical limits
B. They encourage the model to force ambiguous source text into predefined categories even when none truly fit
C. They make JSON invalid when more than five values are listed
D. They prevent null values in every schema language

**Answer:** B
**Explanation:** Large or poorly aligned enums can push the model toward incorrect classification because it must choose from an ill-fitting set. The issue is semantic mismatch, not JSON validity or an inherent null limitation.

### Q13.
A claims-processing team debates whether `claim_denial_reason` should be required. Many approved claims naturally have no denial reason. What is the best recommendation?

A. Keep it required and use `"approved"` as the denial reason for successful claims
B. Make `claim_denial_reason` optional or nullable because it applies only in a subset of cases
C. Remove the field entirely to simplify the schema
D. Populate it from historical approval codes

**Answer:** B
**Explanation:** Conditional data should not be required universally. Optional or nullable fields let approved claims omit denial reasons cleanly, whereas sentinel values or inferred codes mix unrelated concepts and corrupt analytics.

### Q14.
A document pipeline extracts `effective_date`. In some contracts, two dates are plausible: signature date and effective date. The text does not clearly say which controls. What is the safest schema strategy?

A. Require one date and tell the model to choose the earliest
B. Allow null for `effective_date` and optionally capture candidate dates in supporting fields if ambiguity remains unresolved
C. Use the signature date by default because it is usually close enough
D. Concatenate both dates into one string field

**Answer:** B
**Explanation:** When the source does not clearly establish the target field, null plus supporting evidence prevents fabricated certainty. Choosing a default or combining multiple dates into one field undermines data quality and downstream logic.

### Q15.
A team uses the same extractor across multilingual forms. Some locales omit honorifics entirely, while others include titles not seen before. Which schema choice best supports reliable extraction?

A. Require `honorific` and map unfamiliar titles to `Mr`
B. Use a closed enum with only `Mr`, `Mrs`, `Ms`, and `Dr`
C. Make `honorific` optional or nullable, and only use an enum if the downstream domain truly requires a controlled set that matches real inputs
D. Drop the field because variation exists

**Answer:** C
**Explanation:** Optionality handles absence, and enums should only be used when the domain is genuinely controlled and well understood. Forced mappings and narrow enums cause systematic distortion, while dropping the field may discard useful information.

---

[← Back to objectives index](README.md) · [Back to main index](../../README.md)
