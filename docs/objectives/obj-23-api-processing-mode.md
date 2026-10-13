# Objective 23: API Processing Modes

[← Back to objectives index](README.md) · [Back to main index](../../README.md)

> **Exam objective:** Select the appropriate API processing mode—synchronous Messages API or asynchronous Message Batches API—based on latency requirements, workflow blocking behavior, and acceptable processing windows.

---

### Q1.
A chat application needs to display model responses to users in near real time after each message. Which processing mode is the best fit?

A. Asynchronous Message Batches API  
B. Synchronous Messages API  
C. Offline CSV export mode  
D. A nightly batch ETL job

**Answer:** B  
**Explanation:** Interactive chat requires low-latency request/response behavior, which matches the synchronous Messages API. Batch processing introduces queueing and delayed completion, making it unsuitable for immediate user interaction.

### Q2.
A company needs to classify 200,000 archived support tickets overnight, and the workflow does not block any active user experience. Which option is most appropriate?

A. Synchronous Messages API called one ticket at a time from the UI  
B. Asynchronous Message Batches API  
C. Manual copy-paste into a chat window  
D. Streaming tokens to the user

**Answer:** B  
**Explanation:** Large, non-interactive workloads with acceptable processing windows are ideal for asynchronous batching. The synchronous API is better for immediate responses, not overnight back-office throughput.

### Q3.
An expense-report submission form must return a compliance warning before the employee can continue to the next screen. Which mode should you choose?

A. Message Batches API, because it scales better  
B. Synchronous Messages API, because the workflow is blocked pending the result  
C. Either mode, because latency never matters for forms  
D. Message Batches API only if the file is a PDF

**Answer:** B  
**Explanation:** The user cannot proceed until the model's decision is available, so the workflow is latency-sensitive and blocking. That strongly favors a synchronous call pattern.

### Q4.
Which requirement most strongly points to using the Message Batches API instead of the synchronous Messages API?

A. Tokens should stream back as they are generated  
B. The caller must inspect the result before continuing the same request path  
C. Results can arrive later within a broad processing window  
D. The user expects a typing indicator in chat

**Answer:** C  
**Explanation:** The Message Batches API is designed for asynchronous workloads where delayed completion is acceptable. Streaming and immediate branching decisions are better handled synchronously.

### Q5.
A fraud team runs a daily pipeline that enriches 50,000 transactions and writes scores to a database before analysts review them the next morning. Which mode is the most operationally appropriate?

A. Synchronous Messages API embedded in the analyst dashboard  
B. Asynchronous Message Batches API  
C. Browser automation around a chatbot  
D. A human reviewer for every transaction first

**Answer:** B  
**Explanation:** This is a classic scheduled, non-blocking enrichment workload with a clear acceptable window. Asynchronous batches simplify large-scale submission and later result collection.

### Q6.
Your product manager says, "If inference takes more than a few seconds, users abandon the workflow." What is the best interpretation?

A. Prefer asynchronous batching because it handles more items  
B. Prefer the synchronous Messages API because latency is a core user requirement  
C. Use either mode and increase temperature  
D. Delay the whole workflow until the nightly batch completes

**Answer:** B  
**Explanation:** When user abandonment is tied to response delay, latency becomes a primary architecture constraint. That makes the synchronous request/response mode the correct default choice.

### Q7.
A team is split between modes for a document-tagging feature. The tagging is started by a user upload, but the tags are used only in later reporting and do not affect the upload confirmation. Which mode fits best?

A. Synchronous Messages API, because a user initiated the action  
B. Asynchronous Message Batches API, because the workflow is not blocked on the result  
C. Neither; model APIs should only be used for chat  
D. Synchronous only if the upload is under 1 MB

**Answer:** B  
**Explanation:** The critical distinction is not who started the action but whether the result is needed immediately in the active workflow. Since upload confirmation can proceed without waiting, batching is a better fit.

### Q8.
Which architecture is least appropriate for the synchronous Messages API?

A. Real-time assistant reply in a customer chat  
B. Inline moderation check before displaying user content  
C. Overnight summarization of a month of meeting transcripts  
D. A web form that needs instant extraction feedback

**Answer:** C  
**Explanation:** Overnight summarization of large backlogs is precisely the kind of delayed, high-volume workload better suited to batching. The other scenarios all require immediate results in the active request path.

### Q9.
An internal tool must summarize a single uploaded memo while the employee waits on the page. The volume is low, but users expect answers in one interaction. What is the best mode?

A. Asynchronous Message Batches API  
B. Synchronous Messages API  
C. A weekly scheduled export  
D. Randomly switch between modes

**Answer:** B  
**Explanation:** Low-volume, immediate-response scenarios align directly with synchronous invocation. Batch mode would add avoidable complexity and delay without delivering user-visible value.

### Q10.
A data team wants to process millions of records gradually over several hours and poll for completion status later. Which factor most strongly supports asynchronous batching?

A. Need for sub-second end-user latency  
B. Acceptable delayed completion and non-blocking workflow  
C. Requirement to branch UI logic immediately on each result  
D. Need for conversational back-and-forth with a human

**Answer:** B  
**Explanation:** The decisive factor is that completion can happen later without blocking a live interaction. Asynchronous batching is designed for high-volume workloads that tolerate delayed results.

### Q11.
A compliance portal uses a model to decide whether to show an extra attestation screen during form submission. Which API mode is most appropriate?

A. Asynchronous Message Batches API, because compliance workloads are always large  
B. Synchronous Messages API, because the decision affects the current user path  
C. Either mode, because attestation can be shown tomorrow  
D. Batches API only if there are more than 100 users online

**Answer:** B  
**Explanation:** The model output changes the immediate control flow of the current transaction, so the result must be available now. That makes synchronous processing the correct architectural choice.

### Q12.
What is the clearest disadvantage of using the Message Batches API for a live chat product?

A. It cannot handle more than one request  
B. It introduces asynchronous delay incompatible with turn-by-turn interaction  
C. It always costs more  
D. It requires structured output

**Answer:** B  
**Explanation:** Live chat depends on immediate conversational turns, and asynchronous batch completion breaks that experience. The issue is primarily latency and workflow fit, not mandatory structure or a hard request-count limit.

### Q13.
You are deciding between modes for a nightly quality-assurance job that grades 80,000 call transcripts. Which choice best balances architecture and requirements?

A. Synchronous Messages API because each transcript is a separate item  
B. Asynchronous Message Batches API because the job is high-volume and time-flexible  
C. Synchronous Messages API because graders might inspect results tomorrow  
D. Neither mode; only embeddings can grade text

**Answer:** B  
**Explanation:** High-volume, delayed-result workflows are exactly where asynchronous batch processing shines. The fact that each transcript is separate does not imply they should be processed synchronously.

### Q14.
Which statement best captures the decision rule between the two modes?

A. Use synchronous only for short prompts and asynchronous only for long prompts  
B. Use synchronous when the caller is waiting now; use asynchronous when completion can happen later  
C. Use asynchronous for any enterprise use case  
D. Use synchronous unless you need JSON output

**Answer:** B  
**Explanation:** The central architecture decision is driven by latency sensitivity and whether the workflow is blocked pending the result. Prompt length, company size, and JSON needs are secondary and not the core selection criterion.

### Q15.
A team proposes using the synchronous Messages API for a nightly job because "it is simpler to code," even though the job processes hundreds of thousands of independent records and no user is waiting. What is the best response?

A. Agree; simplicity always outweighs workflow fit  
B. Prefer the Message Batches API because the workload is asynchronous by nature and does not require immediate responses  
C. Cancel the job entirely  
D. Move the job into the website request thread

**Answer:** B  
**Explanation:** Architectural fit should follow workload characteristics, not just initial coding convenience. For large non-blocking jobs, batching is the more appropriate operational model and avoids forcing an interactive API shape onto an offline task.

---

[← Back to objectives index](README.md) · [Back to main index](../../README.md)
