# Objective 22: Human Review Routing

[← Back to objectives index](README.md) · [Back to main index](../../README.md)

> **Exam objective:** Design human review routing strategies that direct extractions to reviewers based on confidence scores, document characteristics, and field-level ambiguity rather than random sampling.

---

### Q1.
A mortgage-processing system extracts income, property address, and loan amount from uploaded documents. The team currently sends 10% of records to reviewers at random, but critical field errors still reach production. Which routing strategy is best?

A. Keep random sampling but increase it to 20%  
B. Route records to human review when confidence is low or high-risk fields show ambiguity  
C. Review only the largest files  
D. Review documents only when the customer complains

**Answer:** B  
**Explanation:** Confidence- and ambiguity-based routing focuses human effort where extraction risk is highest. Random sampling can help quality monitoring, but it is inefficient as the primary control for catching risky mistakes.

### Q2.
An ID-verification pipeline extracts date of birth, document number, and issuing country. The model is highly confident overall, but the issuing country field has two plausible values because the passport scan is partially obscured. What should happen?

A. Auto-approve because the overall document confidence is high  
B. Route the entire batch to review  
C. Route this record for review based on field-level ambiguity  
D. Reject the document automatically without review

**Answer:** C  
**Explanation:** Field-level ambiguity is exactly the kind of signal that should trigger targeted human review, even when overall confidence is high. Aggregate confidence can mask a critical uncertainty in one decision-relevant field.

### Q3.
You are designing review queues for invoices. Which record most clearly belongs in the priority human-review queue?

A. A clean machine-generated PDF with high confidence on all required fields  
B. A handwritten scan with low confidence on vendor name and an unreadable total  
C. A duplicate invoice already validated earlier  
D. A small invoice from a trusted vendor with no ambiguous fields

**Answer:** B  
**Explanation:** Handwritten scans and unreadable totals are strong document-characteristic and ambiguity signals for human intervention. The other records present much lower risk and are better candidates for straight-through processing.

### Q4.
A healthcare intake workflow extracts allergy information and emergency contacts. Why is routing based on field criticality important in addition to confidence?

A. Because all fields should always be reviewed the same way  
B. Because a modest-confidence error in a safety-critical field can matter more than a low-confidence error in a minor field  
C. Because criticality makes confidence unnecessary  
D. Because document length is the only reliable signal

**Answer:** B  
**Explanation:** Review policy should combine uncertainty with business impact. A borderline extraction in a safety-critical field may warrant review even if the same confidence would be acceptable for a non-critical field.

### Q5.
A team routes documents for review only when the model's average confidence score is below 0.8. Which weakness is most significant?

A. Average confidence can hide one dangerous low-confidence field inside an otherwise easy document  
B. Reviewers prefer odd numbers  
C. 0.8 is always too high for any use case  
D. Confidence should be ignored in regulated workflows

**Answer:** A  
**Explanation:** Averages can conceal localized failures, such as a wrong account number in an otherwise simple form. Field-level routing avoids this masking problem and better aligns review effort with actual risk.

### Q6.
Two documents have identical confidence scores. One is a crisp digital statement; the other is a phone photo with skew, glare, and handwriting. How should a strong routing system treat them?

A. Treat them identically because confidence is equal  
B. Prefer review for the degraded photo because document characteristics increase extraction risk  
C. Auto-approve both because the score is the same  
D. Reject both without review

**Answer:** B  
**Explanation:** Document characteristics provide additional risk signals beyond model confidence alone. Poor image quality and handwriting commonly increase error likelihood and justify more scrutiny.

### Q7.
You need to reduce reviewer workload without sacrificing quality. Which policy is most efficient?

A. Route every document to review  
B. Review only a fixed random percentage  
C. Review low-confidence or high-ambiguity fields first, and auto-process clear low-risk documents  
D. Eliminate human review entirely

**Answer:** C  
**Explanation:** Targeted routing concentrates limited reviewer time where it produces the most quality improvement. Reviewing everything is expensive, while random-only or zero-review strategies do not align effort with risk.

### Q8.
A claims system extracts claimant name, incident date, and policy number. The policy number field often confuses 0 and O. Which routing enhancement best addresses this issue?

A. Increase max output tokens  
B. Add a field-specific ambiguity rule that flags visually confusable policy numbers for review  
C. Randomly sample more incident dates  
D. Route only claims submitted on Fridays

**Answer:** B  
**Explanation:** This is a classic field-specific ambiguity pattern, and the routing logic should explicitly capture it. General confidence thresholds alone may not reliably detect all visually confusable character errors.

### Q9.
Which approach best supports auditability in a human review routing system?

A. Sending records to review without recording why  
B. Logging the routing reason, such as low confidence, poor scan quality, or ambiguous field match  
C. Allowing each reviewer to decide which records appear in their queue  
D. Deleting confidence metadata after processing

**Answer:** B  
**Explanation:** Auditability requires traceable, explainable routing decisions. Logging the specific signals that triggered review supports compliance, debugging, and threshold tuning over time.

### Q10.
A legal intake pipeline receives both typed forms and scanned handwritten witness statements. Which strategy best reflects objective-aligned routing?

A. Review all typed forms and auto-approve all handwritten statements  
B. Use document type and quality characteristics to send handwritten witness statements to more rigorous review  
C. Ignore document characteristics if the extraction model is modern  
D. Route based only on document upload time

**Answer:** B  
**Explanation:** Different document types and qualities carry different extraction risks. Handwritten witness statements are harder to extract reliably and deserve stronger review routing than clean typed forms.

### Q11.
A tax-prep assistant extracts 40 fields per submission. Review capacity is limited. What is the best design?

A. Review the first 5 fields of every submission  
B. Review fields with the lowest confidence or highest ambiguity, prioritizing high-impact fields such as taxpayer ID and income totals  
C. Review only forms submitted by new customers  
D. Review whichever records happen to be shorter

**Answer:** B  
**Explanation:** When review capacity is scarce, field-level prioritization by uncertainty and business impact delivers the best coverage. Arbitrary slicing by position, customer tenure, or record length is less defensible and less effective.

### Q12.
Why is pure random sampling insufficient as the main review strategy in an extraction pipeline with confidence signals?

A. Random sampling guarantees all important errors are caught  
B. Random sampling ignores the model's uncertainty and document risk features  
C. Random sampling is illegal in all industries  
D. Random sampling can only be used with asynchronous processing

**Answer:** B  
**Explanation:** Confidence scores, ambiguity indicators, and document characteristics are valuable risk signals that random routing wastes. Random sampling can still serve monitoring purposes, but it should not replace risk-based review assignment.

### Q13.
A reviewer queue becomes overwhelmed because too many medium-confidence documents are routed. Which improvement best preserves quality while reducing volume?

A. Remove all thresholds and trust the model completely  
B. Introduce field-criticality weighting so only ambiguous high-impact fields escalate at medium confidence  
C. Route by alphabetical order of customer name  
D. Review only PDFs and ignore images

**Answer:** B  
**Explanation:** Not every medium-confidence field deserves equal treatment. Weighting by field importance allows the system to escalate meaningful risk while avoiding unnecessary review for low-impact uncertainties.

### Q14.
An insurance company wants a secondary expert review only when the first reviewer sees ambiguity in injury severity extraction from narrative reports. What does this illustrate?

A. Random double-sampling  
B. Multi-stage routing driven by field-level ambiguity  
C. A prompt-only extraction design  
D. Sliding-window context management

**Answer:** B  
**Explanation:** The second review is triggered by a specific ambiguity condition, which is a targeted routing design. It adds human oversight where uncertainty remains after the first pass instead of applying blanket escalation.

### Q15.
Which policy best aligns with the exam objective for production extraction systems?

A. Review documents randomly to appear fair  
B. Route reviews using confidence thresholds, document-type risk, and field-level ambiguity rules  
C. Review only when the model explicitly asks for help  
D. Approve everything above one global confidence score regardless of field type

**Answer:** B  
**Explanation:** The objective emphasizes routing by risk signals: confidence, document characteristics, and ambiguity at the field level. Randomness or one-size-fits-all thresholds fail to capture the real structure of extraction risk.

---

[← Back to objectives index](README.md) · [Back to main index](../../README.md)
