# Objective 20: Context Management Strategies

[← Back to objectives index](README.md) · [Back to main index](../../README.md)

> **Exam objective:** Apply context management strategies—subagent isolation, scratchpad files, and targeted file reading—to sustain coherent codebase exploration across sessions exceeding context limits.

---

### Q1.
You are analyzing a very large monorepo and know the investigation will exceed one context window. Which approach best preserves coherence from the start?

A. Read as much as possible before taking any notes  
B. Split independent threads into subagents, keep concise scratch summaries, and read files selectively  
C. Avoid subagents because they create too much structure  
D. Restart the investigation whenever context fills  

**Answer:** B  
**Explanation:** Large explorations require deliberate context control, including isolation of separate threads and compact summaries of what matters. Blind accumulation or repeated restarts loses continuity and wastes effort.

### Q2.
What is the main value of subagent isolation in context management?

A. It guarantees the parent agent never needs to synthesize results  
B. It prevents unrelated investigative threads from crowding each other out in a single context window  
C. It removes the need for targeted reading  
D. It automatically verifies all findings  

**Answer:** B  
**Explanation:** Separate agents can hold distinct working sets, allowing each thread to stay coherent without contaminating the others. The parent still must synthesize, but with cleaner, more focused inputs.

### Q3.
When should you prefer a scratchpad file during a long exploration?

A. When you need to preserve evolving findings, hypotheses, and next steps beyond immediate context capacity  
B. Only when writing user-facing documentation  
C. Only after all exploration is finished  
D. Never, because scratchpads always waste time  

**Answer:** A  
**Explanation:** Scratchpads are valuable for retaining the distilled state of an investigation across long sessions or context compaction events. They are not just for final documentation; they preserve continuity during the work itself.

### Q4.
Why is targeted file reading a context-management technique, not just a search preference?

A. Because reading only high-value files or sections preserves room for reasoning and synthesis  
B. Because targeted reading is always faster than any other method  
C. Because large files cannot be opened  
D. Because search tools are unreliable  

**Answer:** A  
**Explanation:** Context is consumed by what you read, so precision in file selection directly affects how much reasoning capacity remains. Speed may help, but the core issue is information density and relevance.

### Q5.
You have three mostly independent questions: auth flow, deployment pipeline, and caching behavior. What is the best strategy?

A. Mix all searches in one running narrative so connections emerge naturally  
B. Delegate each thread to its own subagent or at least separate workstream, then synthesize results centrally  
C. Focus on whichever thread has the most files and ignore the rest  
D. Read the entire repo before separating concerns  

**Answer:** B  
**Explanation:** Independent threads are prime candidates for isolation so each can develop a coherent local model. The parent can later integrate them without having all details compete in the same context window.

### Q6.
During a long session, your context window is nearly full, but you still need to continue a specific symbol trace. What is the best move?

A. Compact or externalize the key findings, then continue from the active frontier with targeted reads  
B. Keep reading until the model starts forgetting details  
C. Start a completely unrelated investigation to clear the buffer  
D. Reopen every file from the beginning  

**Answer:** A  
**Explanation:** Before context degrades further, preserve the important state in concise form and proceed only with the next relevant steps. This protects continuity and avoids unnecessary rework.

### Q7.
What should a good exploration scratchpad contain?

A. Full copies of every file read  
B. Distilled findings, unresolved questions, important paths, and next investigative steps  
C. Only personal reminders unrelated to the task  
D. Random excerpts in the order discovered  

**Answer:** B  
**Explanation:** A scratchpad should compress the investigation into the minimum state needed to resume intelligently. Full file copies defeat the purpose and consume unnecessary space and attention.

### Q8.
Which practice best reduces the chance of losing a valuable insight when switching between sessions?

A. Trust memory instead of writing anything down  
B. Maintain a compact persisted summary of confirmed facts and open questions  
C. Reread the entire codebase at the start of each session  
D. Avoid investigating anything complex near the context limit  

**Answer:** B  
**Explanation:** Persisted summaries bridge session boundaries efficiently and reliably. Re-reading everything is costly, and relying on memory alone is error-prone in large investigations.

### Q9.
Why is it often helpful for the parent agent to request structured summaries from subagents instead of raw transcripts?

A. Structured summaries compress the essential state while minimizing cross-thread context load  
B. Raw transcripts are invalid inputs  
C. Structured summaries always contain every detail  
D. It prevents subagents from citing sources  

**Answer:** A  
**Explanation:** Context management depends on compression with fidelity. Structured outputs make it easier to carry forward only the relevant conclusions, evidence, and open issues from each subagent.

### Q10.
You are investigating a bug that touches one service deeply and a second service only tangentially. How should context be allocated?

A. Read both services with equal depth to be fair  
B. Go deep on the primary service and keep the secondary service investigation narrow unless evidence justifies expansion  
C. Ignore the primary service because it is already the obvious suspect  
D. Avoid reading code and rely on issue descriptions  

**Answer:** B  
**Explanation:** Good context management allocates attention proportionally to expected relevance. This reduces waste while still leaving room to expand if the evidence later points more strongly to the secondary service.

### Q11.
What is a key advantage of resuming from a scratchpad plus targeted reads after context compaction?

A. It guarantees no detail was ever omitted  
B. It restores the investigation's working model efficiently without replaying every prior step  
C. It makes search tools unnecessary  
D. It prevents new hypotheses from forming  

**Answer:** B  
**Explanation:** Compaction is effective when the essential model has already been distilled somewhere durable. You can then rebuild active context from the frontier rather than from the entire exploration history.

### Q12.
Which behavior most likely signals poor context management?

A. Narrowing reads to the files on the current symbol path  
B. Keeping separate summaries for parallel investigation threads  
C. Repeatedly opening large unrelated files because they might become useful later  
D. Delegating an isolated subsystem to a subagent  

**Answer:** C  
**Explanation:** Reading speculative low-relevance material is a common way to exhaust context without increasing understanding. The other choices all help preserve focus and continuity.

### Q13.
How do subagent isolation and scratchpads complement each other?

A. They solve the same problem, so only one should ever be used  
B. Subagents isolate active reasoning; scratchpads preserve the distilled outputs and handoff state  
C. Scratchpads replace all synthesis work  
D. Subagents are only useful when no files are available  

**Answer:** B  
**Explanation:** Isolation helps during exploration, while scratchpads help across boundaries—between agents, between phases, or between sessions. Together they reduce context interference and improve resumability.

### Q14.
In a multi-day investigation, what is the best reason to prefer targeted section reads over full-file rereads when resuming?

A. Section reads help rehydrate only the immediately relevant implementation details without reconsuming large amounts of context  
B. Full-file rereads are always impossible  
C. Section reads automatically update the scratchpad  
D. They eliminate all uncertainty about file behavior  

**Answer:** A  
**Explanation:** Resumption is about recovering the current frontier cheaply. Targeted reads refresh the exact details needed to continue, while full-file rereads often consume context on already-settled material.

### Q15.
Which end-to-end workflow best reflects strong context management on a large codebase?

A. Open many files opportunistically, rely on memory, and summarize only at the end  
B. Partition independent threads, gather focused evidence, maintain concise scratch state, and synthesize periodically  
C. Avoid delegation and read everything sequentially  
D. Compact context only after information has already been lost  

**Answer:** B  
**Explanation:** Strong context management is proactive: isolate threads, read with intent, preserve distilled state, and synthesize before the working set becomes unstable. The other workflows are reactive and prone to lost continuity.

---

[← Back to objectives index](README.md) · [Back to main index](../../README.md)
