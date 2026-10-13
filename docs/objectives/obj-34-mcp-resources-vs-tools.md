# Objective 34: MCP Resources vs. Tools

[← Back to objectives index](README.md) · [Back to main index](../../README.md)

> **Exam objective:** Distinguish between MCP resources and tools, and expose server content as resources to reduce exploratory tool calls and improve agent efficiency in cross-system queries.

---

### Q1.
An MCP server exposes a static catalog of internal APIs that agents frequently browse before deciding what action to take. What is the best way to expose this catalog?

A. As a tool that requires a call for every lookup
B. As a resource the agent can read directly
C. Only through Bash commands on the server host
D. As a hidden prompt example

**Answer:** B
**Explanation:** Static or reference content that agents need to inspect is usually better exposed as a resource, because it reduces unnecessary exploratory tool calls. Tools are better reserved for actions or computations.

### Q2.
Which statement best distinguishes MCP resources from MCP tools?

A. Resources are for readable content or state representation, while tools are for actions, operations, or parameterized execution
B. Resources can modify remote systems, but tools cannot
C. Tools are only for local files, while resources are only for APIs
D. There is no meaningful difference; they are interchangeable

**Answer:** A
**Explanation:** Resources primarily expose information to be consumed, while tools are designed for invoking behavior. The other choices reverse responsibilities or collapse an important distinction.

### Q3.
A server exposes a product inventory table. Agents often call a search tool repeatedly just to understand the available categories before asking targeted questions. What redesign best improves efficiency?

A. Remove the search tool entirely
B. Expose the inventory schema or category listing as a resource, while keeping search as a tool for targeted retrieval
C. Force agents to guess categories from prior examples
D. Convert all inventory access into a single shell command

**Answer:** B
**Explanation:** Making the catalog structure available as a resource gives the agent orienting context without repeated exploratory calls. The search tool still has value for targeted operations once the agent knows what to ask.

### Q4.
You are integrating a CRM MCP server. Which item is the best candidate for a resource rather than a tool?

A. "Create lead" operation
B. "Update opportunity stage" operation
C. A list of field definitions, picklist values, and object descriptions
D. "Delete duplicate contact" action

**Answer:** C
**Explanation:** Metadata and reference descriptions are classic resource content because agents read them to understand the system. The other items are state-changing or action-oriented and belong as tools.

### Q5.
Why can exposing server content as resources reduce exploratory tool calls?

A. Because resources make the model deterministic
B. Because the agent can inspect available data structures and documentation directly instead of calling tools merely to discover what exists
C. Because tools become unnecessary in all integrations
D. Because resources automatically cache every future answer

**Answer:** B
**Explanation:** Resources provide ambient discoverability for reference content, eliminating many "what data is here?" tool calls. They do not remove the need for tools, guarantee determinism, or solve all caching concerns.

### Q6.
A cross-system workflow needs to compare ticket fields from a support platform and status values from a deployment system. What MCP design most helps the agent reason efficiently before acting?

A. Expose both systems only through mutation tools
B. Expose each system's schemas and enumerations as resources, then provide tools for the actual queries or updates
C. Hide field names and require agents to infer them
D. Use one generic "do anything" tool with a free-form prompt

**Answer:** B
**Explanation:** Resources provide the structural context needed for accurate cross-system reasoning, while tools remain available for operations. The other designs increase ambiguity, unnecessary exploration, or unsafe overbreadth.

### Q7.
Which scenario most clearly indicates that something should be a resource instead of a tool?

A. The agent must submit a change request with parameters
B. The agent needs to read a stable reference manual that rarely changes and is used mainly for orientation
C. The agent must trigger a deployment pipeline
D. The agent needs to rotate credentials

**Answer:** B
**Explanation:** Stable reference content that supports understanding is a strong fit for a resource. The other scenarios are clearly action-oriented and therefore better suited to tools.

### Q8.
An architect exposes a database schema only through a `describe_table(name)` tool. Agents frequently call it repeatedly across many tables just to learn the data model. What is the best improvement?

A. Increase the tool timeout
B. Add a resource that exposes the schema catalog or table index, keeping detailed tools for deeper inspection when needed
C. Remove schema access entirely
D. Replace the tool with a deployment script

**Answer:** B
**Explanation:** A schema catalog resource gives the agent cheap visibility into the broader structure, reducing repetitive discovery calls. Detailed tools can still be used for narrower follow-up actions or retrieval.

### Q9.
Which choice is the strongest reason not to expose every piece of server content only as tools?

A. Tools are incapable of returning text
B. It forces agents to spend actions discovering static information that could be made directly readable as context
C. Tools cannot accept parameters
D. Resources are always more secure than tools

**Answer:** B
**Explanation:** When reference data is hidden behind tools, agents often waste actions just discovering the landscape. The other statements are false or too absolute.

### Q10.
What is the best design for a knowledge-base MCP server whose articles are frequently read, while article submission is rare and state-changing?

A. Expose articles as resources and submission as a tool
B. Expose articles only through a submit tool
C. Expose submission as a resource and articles as tools
D. Expose neither; put everything in the system prompt

**Answer:** A
**Explanation:** Read-heavy reference content belongs naturally in resources, while state-changing submission remains an action and should be modeled as a tool. This separation matches usage patterns and improves efficiency.

### Q11.
An agent needs to answer, "What environments exist, and which deployment statuses are valid in each system?" before making any changes. Which MCP setup is best?

A. Only mutation tools for deployments
B. Environment and status vocabularies exposed as resources, with tools reserved for later operational calls
C. One opaque tool that decides everything internally
D. No MCP integration at all

**Answer:** B
**Explanation:** The question is primarily exploratory and comparative, so readable vocabularies and schemas should be directly exposed as resources. Tools remain useful later if the workflow proceeds to action.

### Q12.
Which anti-pattern most directly conflicts with this objective?

A. Publishing server documentation as a resource
B. Modeling a search endpoint as a tool
C. Requiring the agent to call tools repeatedly just to enumerate available content that could have been exposed as a resource
D. Separating reference content from state-changing operations

**Answer:** C
**Explanation:** The objective explicitly seeks to reduce exploratory tool calls by exposing content as resources where appropriate. The other options either align with the objective or are neutral design choices.

### Q13.
An MCP server offers a list of supported report types and a `generate_report(type, range)` operation. How should these be exposed?

A. Both as resources
B. Both as tools
C. Supported report types as a resource; report generation as a tool
D. Supported report types in examples only; generation as a resource

**Answer:** C
**Explanation:** The available report taxonomy is reference information and should be readable as a resource. Generating a report is a parameterized operation, so it belongs as a tool.

### Q14.
What is the main benefit of exposing schemas, catalogs, and documentation as resources in cross-system queries?

A. Agents can build better mental models of each system before choosing which tool actions to take
B. Resources can perform writes faster than tools
C. It removes the need for authentication
D. It guarantees perfect joins across systems

**Answer:** A
**Explanation:** Cross-system tasks often fail from poor system understanding, so making structure visible up front improves query planning and reduces wandering. Resources do not perform writes, remove auth, or guarantee perfect data mapping.

### Q15.
You observe that agents call `list_projects`, `list_environments`, and `list_statuses` at the start of nearly every run, even when those values rarely change. What redesign best matches the exam objective?

A. Leave the design unchanged because repeated tool calls prove the tools are useful
B. Replace those discovery-oriented lists with readable resources, while keeping action-oriented or parameterized operations as tools
C. Combine the three tools into one larger tool and keep it mandatory
D. Disable access to projects, environments, and statuses entirely

**Answer:** B
**Explanation:** Repeated discovery calls for mostly stable reference data are a strong signal that the information should be exposed as resources. This reduces overhead while preserving tools for true operational tasks.

---

[← Back to objectives index](README.md) · [Back to main index](../../README.md)
