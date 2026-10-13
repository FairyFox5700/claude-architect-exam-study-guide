# Objective 31: Inclusion and Exclusion Boundaries

[← Back to objectives index](README.md) · [Back to main index](../../README.md)

> **Exam objective:** Design prompt criteria that define explicit inclusion and exclusion boundaries, preventing the model from generating findings or extractions in categories where performance is unreliable.

---

### Q1.
A compliance team wants Claude to extract only contractual payment terms from vendor agreements. The model has been incorrectly extracting informal negotiation comments from email threads embedded in the documents. Which prompt revision best establishes the needed boundary?

A. "Extract all financial information and include anything that looks relevant."
B. "Extract payment obligations, due dates, currencies, and late-fee clauses from executed contract sections only. Exclude emails, comments, tracked changes, and negotiation notes."
C. "Focus on payment details, but use your judgment if surrounding discussion seems useful."
D. "Summarize the whole agreement and list the most important money-related facts."

**Answer:** B
**Explanation:** B defines both what to include and what to exclude, reducing ambiguity around unreliable sources like embedded commentary. The other options invite interpretation, broaden scope, or convert the task into summarization instead of controlled extraction.

### Q2.
You are designing a prompt for incident-ticket triage. The model is good at recognizing outage severity from structured fields, but unreliable at inferring business impact from free-form customer frustration. What is the best instruction?

A. "Classify severity from any evidence you can find in the ticket."
B. "Use structured severity indicators first, but you may upgrade severity if the customer sounds upset."
C. "Determine severity only from explicit structured indicators such as impact field, affected region count, and SLA flag. Do not infer severity from tone, sentiment, or wording intensity."
D. "Assign the worst-case severity when the ticket is unclear."

**Answer:** C
**Explanation:** C restricts the model to reliable signals and explicitly excludes an unreliable category: emotional tone. A and B encourage unsupported inference, while D introduces a risky escalation rule unrelated to actual evidence.

### Q3.
A legal operations team asks for clause extraction from contracts, but the model often hallucinates missing indemnity clauses when language is similar but not equivalent. Which prompt addition is best?

A. "If an indemnity clause seems implied, extract it."
B. "Extract indemnity clauses and similar protections."
C. "Extract text only when the document explicitly states indemnification obligations. Do not label limitation-of-liability, insurance, or warranty language as indemnity unless the obligation is directly expressed."
D. "Capture all risk-transfer concepts in one combined field."

**Answer:** C
**Explanation:** C creates a precise semantic boundary around explicit indemnity language and excludes neighboring concepts that are often confused. The other options broaden the category and increase false positives.

### Q4.
An HR team uses Claude to identify policy violations in employee chat logs. Testing shows reliable detection of explicit threats but poor performance on sarcasm and coded jokes. Which instruction best aligns to the objective?

A. "Flag any message that feels inappropriate."
B. "Flag explicit threats, direct harassment, and clearly stated policy violations. Exclude sarcastic interpretation, coded humor, and implied intent unless the violation is directly stated."
C. "Use context to infer hidden hostility wherever possible."
D. "Err on the side of flagging more content for reviewer safety."

**Answer:** B
**Explanation:** B keeps the model within reliable detection categories and bars weak inference on sarcasm and coded language. A, C, and D all encourage overinclusive behavior in areas the model performs unreliably.

### Q5.
You must extract product defects from support cases. The model performs well on reproducible failures but poorly on user speculation about root cause. Which prompt is strongest?

A. "Capture defects and likely causes."
B. "Extract any technical observation related to the problem."
C. "Extract observed product failures, error messages, reproduction steps, and confirmed system behavior. Exclude customer guesses, agent hypotheses, and unverified root-cause speculation."
D. "Summarize what probably went wrong."

**Answer:** C
**Explanation:** C separates reliable observations from unreliable speculation, which is exactly the boundary required. The other options blend evidence with inference and would likely increase noisy outputs.

### Q6.
A prompt says, "Extract security issues from code review comments." Results include style suggestions labeled as security findings. What missing element most directly caused the problem?

A. A requirement to produce JSON output
B. An explicit exclusion list defining what is not a security issue
C. A higher temperature setting
D. A request for longer explanations

**Answer:** B
**Explanation:** Without exclusion boundaries, adjacent categories like style, maintainability, and performance can be misclassified as security issues. Output format, temperature, and explanation length do not solve the core categorization ambiguity by themselves.

### Q7.
A medical-document workflow must extract confirmed diagnoses but avoid symptoms, suspected conditions, and ruled-out conditions. Which instruction is best?

A. "Extract all medical conditions mentioned."
B. "List diagnoses and anything clinically important."
C. "Extract confirmed diagnoses documented as active or historical conditions. Exclude symptoms, differential diagnoses, suspected conditions, family history, and ruled-out conditions."
D. "Capture the patient's main health concerns."

**Answer:** C
**Explanation:** C clearly distinguishes the target category from several nearby non-target categories that are easy to confuse. The other options are too broad and would predictably cause over-extraction.

### Q8.
An operations analyst asks why a boundary-focused prompt is preferable to "use common sense" guidance. Which is the best answer?

A. Because common sense prompts always reduce token usage
B. Because explicit boundaries reduce reliance on latent judgment in categories where the model is known to be inconsistent
C. Because common sense disables tool use
D. Because explicit boundaries guarantee perfect recall

**Answer:** B
**Explanation:** Boundary-focused prompts work by constraining the model away from subjective inference in unreliable areas. They do not inherently reduce tokens, disable tools, or guarantee perfect recall.

### Q9.
You are revising a prompt after evaluation shows false positives from extracting "customer commitments" out of internal action items written by the seller. What change best addresses the issue?

A. "Extract commitments more carefully."
B. "Extract all next steps and identify who owns them."
C. "Extract commitments only when the customer explicitly agrees to an action or deliverable. Exclude seller tasks, internal follow-ups, proposed actions, and tentative suggestions."
D. "Lower the model temperature and keep the same instructions."

**Answer:** C
**Explanation:** C targets the exact confusion by separating customer commitments from nearby action-oriented text. A and D are too weak, and B changes the task instead of controlling the extraction boundary.

### Q10.
For a financial-reporting workflow, Claude is reliable at extracting stated revenue figures from tables but unreliable at computing derived metrics across sections. Which prompt design is best?

A. "Extract and calculate all important financial metrics."
B. "Find every number and infer the most useful ratios."
C. "Extract explicitly reported revenue figures, period labels, and table units. Do not calculate margins, growth rates, or derived metrics unless the document states them directly."
D. "Summarize the company's financial performance."

**Answer:** C
**Explanation:** C limits output to directly supported values and excludes computations known to be error-prone in this workflow. The other options invite derivation, interpretation, or summarization beyond the reliable boundary.

### Q11.
During prompt review, a teammate proposes: "If you're not sure whether text belongs, include it and let the reviewer decide." What is the strongest objection?

A. It may increase reviewer workload by systematically reintroducing categories the prompt was supposed to exclude
B. It is always better to maximize recall than precision
C. It prevents the model from reading the document carefully
D. It only works for classification tasks, not extraction tasks

**Answer:** A
**Explanation:** The whole purpose of explicit boundaries is to prevent unreliable categories from entering the output stream. B is not universally true, C is unsupported, and D is incorrect because boundary design applies to both classification and extraction.

### Q12.
You need a prompt for extracting "board-approved decisions" from meeting minutes. The model often includes proposals and discussion points. Which wording is best?

A. "Extract important decisions from the minutes."
B. "Extract proposals, decisions, and next steps."
C. "Extract decisions only when the minutes indicate approval, adoption, or formal acceptance by the board. Exclude proposals, discussion items, recommendations, and unresolved motions."
D. "Identify the outcomes of each agenda item."

**Answer:** C
**Explanation:** C hinges extraction on explicit approval language and excludes nearby concepts that are not finalized decisions. The alternatives are broader and would allow the same proposal-versus-decision confusion to continue.

### Q13.
Which evaluation result most strongly suggests your prompt lacks adequate exclusion boundaries?

A. High precision and low recall on the target category
B. Frequent extraction of adjacent-but-invalid categories that look superficially similar to the target
C. Slight variation in output ordering between runs
D. Correct answers with short explanations

**Answer:** B
**Explanation:** When the model repeatedly includes neighboring categories, it usually means the prompt failed to define what must be left out. The other results do not specifically indicate a boundary-definition problem.

### Q14.
You are designing a prompt for extracting "binding deadlines" from procurement documents. Which instruction best prevents overreach?

A. "Capture all dates related to the procurement process."
B. "Extract binding submission, response, award, and performance deadlines that the document explicitly imposes. Exclude illustrative timelines, historical dates, meeting invites, and optional target dates."
C. "List the most relevant dates and explain why they matter."
D. "Infer which dates the vendor should probably track."

**Answer:** B
**Explanation:** B draws a clean line between mandatory deadlines and other date mentions that are easy to misinterpret. A, C, and D all broaden the scope and invite subjective judgment.

### Q15.
An architect says, "We'll fix unreliable categories later in post-processing instead of in the prompt." What is the best response?

A. That is ideal because prompts should stay as general as possible
B. Prompt-level inclusion and exclusion criteria should be the first control, because they reduce invalid generations before they must be filtered downstream
C. Post-processing always catches every boundary mistake
D. Boundaries only matter when using external tools

**Answer:** B
**Explanation:** Preventing invalid outputs at generation time is usually more reliable and efficient than trying to clean them up later. A, C, and D all understate the value of prompt design as the primary control surface.

---

[← Back to objectives index](README.md) · [Back to main index](../../README.md)
