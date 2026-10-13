# Objective 21: Context Window Optimization

[← Back to objectives index](README.md) · [Back to main index](../../README.md)

> **Exam objective:** Apply context window optimization techniques—summarization, sliding windows, structured state objects, and selective retention—to maintain response quality as conversations exceed practical token limits.

---

### Q1.
A support chatbot helps users troubleshoot a SaaS product over sessions that often exceed 150 turns. Late in the conversation, the model starts forgetting which environment the customer is using and repeats previously eliminated causes. Which design is most likely to preserve response quality?

A. Increase temperature so the model explores more possibilities  
B. Replace the entire history with the last user message only  
C. Maintain a structured state object for durable facts plus rolling summaries of resolved steps  
D. Ask the user to restate the full issue every 20 turns

**Answer:** C  
**Explanation:** A structured state object preserves stable facts like account tier, environment, and confirmed findings, while rolling summaries retain recent reasoning without carrying every old token. Higher temperature worsens consistency, and dropping history or forcing constant restatement degrades the user experience and accuracy.

### Q2.
You are building a document analysis agent that processes 300-page contracts in multiple conversational passes. The final pass must remember only unresolved clauses and approved findings from earlier passes. Which technique is the best fit?

A. Full transcript replay for every pass  
B. Selective retention of only still-relevant artifacts  
C. Random truncation of the earliest context  
D. Storing all extracted text in the system prompt

**Answer:** B  
**Explanation:** Selective retention keeps only unresolved clauses and approved findings, which are the exact items needed later. Full replay is wasteful, random truncation is unsafe, and stuffing all text into the system prompt causes token pressure without prioritization.

### Q3.
A coding assistant works well for the first 20 messages but degrades after long debugging sessions. You want it to retain only the most recent stack traces and code diffs while keeping a compact memory of prior hypotheses. What pattern best matches this need?

A. Sliding window for recent details plus summary memory for older reasoning  
B. Single static prompt with no updates  
C. Tool use disabled so the model focuses on fewer tasks  
D. Chain-of-thought exposure in every response

**Answer:** A  
**Explanation:** A sliding window preserves the freshest technical details, while summaries capture prior attempted fixes and conclusions. A static prompt cannot adapt, and the other choices do not address long-context management.

### Q4.
An operations assistant tracks an outage over a 4-hour conversation. Which item is the best candidate for a structured state object rather than repeated free-text history?

A. The exact wording of every apology sent to stakeholders  
B. A list of confirmed impacted services, current severity, and latest mitigation status  
C. All prior model responses in raw form  
D. Every log line collected during the incident

**Answer:** B  
**Explanation:** Structured state objects work best for durable, frequently referenced facts such as severity, scope, and mitigation status. Raw history and exhaustive logs are expensive and harder for the model to reliably use at scale.

### Q5.
During a long research workflow, the assistant summarizes every five turns. However, later answers omit important caveats from early evidence. What is the most likely flaw?

A. The model should never summarize anything  
B. The summaries are lossy and omit decision-critical details that should have been retained explicitly  
C. The user asked too many questions  
D. The context window is too large

**Answer:** B  
**Explanation:** Summaries are useful but can introduce information loss if critical caveats are not preserved in a durable form. The fix is better summary design and selective retention of high-value exceptions, not abandoning summarization altogether.

### Q6.
You need to preserve accuracy in a compliance workflow where the model must remember the latest approved policy version, the governing jurisdiction, and open review items across many turns. Which approach is most robust?

A. Keep only the last three messages  
B. Store these durable fields in a structured state object updated after each review step  
C. Ask the model to infer them from memory  
D. Put them in a one-time initial user prompt and never mention them again

**Answer:** B  
**Explanation:** Durable, high-importance fields belong in an explicitly updated state object so they remain accessible and consistent. Short windows and one-time mentions rely too heavily on model recall and fail in long conversations.

### Q7.
A team uses a sliding window alone for a procurement assistant. The assistant loses track of an executive approval granted 80 turns earlier and re-asks for it. Which improvement best addresses this specific failure?

A. Expand the sliding window indefinitely  
B. Add selective retention for durable approvals outside the rolling window  
C. Lower the max output tokens  
D. Use a more conversational tone

**Answer:** B  
**Explanation:** Sliding windows are optimized for recency, so older but still-important approvals should be retained separately as durable state. Indefinitely expanding the window eventually recreates the original token-limit problem.

### Q8.
An analyst wants to summarize old conversation chunks into bullet points. Which summary style is best for later reliable reuse by the model?

A. Vague narrative focused on tone and style  
B. Structured bullets covering facts, decisions, unresolved questions, and constraints  
C. One sentence that says "previous details discussed earlier"  
D. A paraphrase that removes numbers and dates to save tokens

**Answer:** B  
**Explanation:** Summaries are most reusable when they preserve operationally important categories such as decisions, constraints, and open questions. Removing specifics like numbers and dates often deletes exactly the details future turns need.

### Q9.
You are designing a multi-agent workflow where one agent interviews a user and another agent drafts a final recommendation later. What is the best handoff artifact for context efficiency and reliability?

A. The complete raw transcript only  
B. A structured state object plus a concise summary of rationale and outstanding risks  
C. No handoff artifact; let the second agent start fresh  
D. A screenshot of the prior chat

**Answer:** B  
**Explanation:** A state object captures durable facts cleanly, and a concise rationale summary preserves reasoning context without replaying everything. Raw transcripts are expensive, while no handoff or screenshots reduce machine readability and accuracy.

### Q10.
A financial assistant conversation contains thousands of tokens of historical market commentary, but the current task only requires the user's portfolio constraints and the last two recommendations. What should the system do?

A. Retain all historical commentary because more context is always better  
B. Selectively retain only the constraints and the still-relevant recent recommendations  
C. Delete all context before answering  
D. Convert the historical commentary into longer prose summaries each turn

**Answer:** B  
**Explanation:** Context should be retained based on current task relevance, not sentiment that more is always better. The portfolio constraints and recent recommendations are decision-critical; old commentary is mostly noise for this task.

### Q11.
Which scenario most strongly suggests using a sliding window rather than only periodic summarization?

A. The task depends heavily on the exact wording of the most recent 10 exchanges  
B. The task never references recent turns directly  
C. The conversation is always under 5 turns  
D. The only requirement is to preserve a user profile for future sessions

**Answer:** A  
**Explanation:** Sliding windows are ideal when precise recent wording still matters, such as active debugging or negotiation. Summaries compress context, which can blur exact phrasing needed for near-term reasoning.

### Q12.
An assistant stores every extracted fact forever to avoid losing information. Over time, responses become slower and less accurate because contradictory outdated facts remain in context. Which principle was neglected?

A. Selective retention should remove stale or superseded information  
B. More persistent memory always improves accuracy  
C. Summaries should be longer than source material  
D. The model should not use context at all

**Answer:** A  
**Explanation:** Retention must be selective not just in what is kept, but also in what is pruned when it becomes obsolete. Keeping stale facts creates conflict and noise, which harms downstream reasoning.

### Q13.
A sales-assistant transcript is nearing token limits. The next step is generating a renewal proposal using customer goals, discount constraints, unresolved objections, and the latest quoted price. Which compaction strategy is best?

A. Preserve every greeting and scheduling exchange  
B. Summarize old conversational filler, keep recent pricing details, and store durable constraints in structured fields  
C. Drop all objections because they are old  
D. Replace the transcript with a generic account summary only

**Answer:** B  
**Explanation:** Proposal quality depends on durable business constraints and exact current commercial details, not every social exchange. This combination of summarization, recency preservation, and structured state directly matches the task.

### Q14.
Which metric most directly indicates that your context optimization strategy is failing in long conversations?

A. The model uses shorter sentences over time  
B. The model begins contradicting previously confirmed facts and re-opening resolved issues  
C. The user sends longer messages  
D. The API response time varies by a few hundred milliseconds

**Answer:** B  
**Explanation:** Contradictions and repeated reopening of resolved issues show that the model is no longer reliably grounding on prior state. Sentence length and minor latency variation are weak or indirect signals compared with factual inconsistency.

### Q15.
You are asked to choose between two designs for a long-running case-management assistant. Design A stores the full transcript only. Design B stores a sliding window, a case-state JSON object, and milestone summaries after each phase. Which design best aligns with context window optimization principles?

A. Design A, because raw transcripts preserve maximum detail  
B. Design B, because it separates durable state, recent detail, and compressed history  
C. Design A, because summaries should never replace original content  
D. Neither design; long-running assistants should not persist context

**Answer:** B  
**Explanation:** Design B explicitly matches best practices for long conversations by preserving different kinds of information in the most efficient form. Raw transcripts alone are costly and make it harder for the model to consistently retrieve what matters.

---

[← Back to objectives index](README.md) · [Back to main index](../../README.md)
