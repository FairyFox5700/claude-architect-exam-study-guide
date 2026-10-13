# Section 5: Model Context Protocol (MCP) Integration & Tool Design

[← Back to index](../README.md)

## Exam objectives covered

1. Distinguish between MCP resources and tools, and expose server content as resources to reduce exploratory tool calls and improve agent efficiency in cross-system queries.
2. Integrate MCP servers into Claude Code and agent applications by selecting the correct server scope, configuring authentication via environment variable expansion, and verifying tool discovery.
3. Write MCP tool descriptions that clearly distinguish each tool's purpose, input formats, use-case boundaries, and relationships to semantically similar tools, reducing misrouting and incorrect tool selection.
4. Configure the `tool_choice` parameter to guarantee tool invocation when structured output is required, and sequence multi-tool workflows so prerequisite data is obtained before dependent tools are called.

This section also covers broader MCP architecture concepts tested on the exam: client/server/host roles, transport mechanisms (stdio vs. HTTP/SSE), server scopes (local/project/user), authentication patterns, and tool naming/namespacing conventions.

---

### Q1. In MCP, which pairing correctly matches the roles of **host**, **client**, and **server**?

A. Host executes tools directly, client stores prompts, server renders UI
B. Host is the user-facing application, client manages MCP connections, server exposes tools/resources/prompts
C. Host is the transport layer, client is the model, server is the filesystem
D. Host and client are interchangeable terms; only the server has a distinct role

**Answer:** B
**Explanation:** The **host** is the application the user interacts with, the **client** is the MCP-aware component inside that host that connects to servers, and the **server** exposes capabilities such as tools, resources, and prompts. A, C, and D confuse implementation layers or collapse roles that are intentionally separated in MCP architecture.

### Q2. Which statement best distinguishes an MCP **resource** from an MCP **tool**?

A. A resource always mutates external state, while a tool is read-only
B. A resource is primarily retrieved or read by the model, while a tool is invoked to perform an action or computation
C. A resource is only for local files, while a tool is only for remote APIs
D. A resource is invisible to the model unless a tool calls it first

**Answer:** B
**Explanation:** Resources are best for exposing structured or reference content that the model can read directly, while tools are for actions, procedures, or dynamic operations. A reverses the usual distinction, C is false because both can represent local or remote systems, and D is incorrect because resources can be directly surfaced to the model.

### Q3. A team exposes a CRM schema, account catalog, and reporting glossary through read-only MCP resources instead of separate "list" tools. What is the main benefit?

A. It guarantees that no tools will ever be needed
B. It reduces exploratory tool calls and gives the model more context up front for cross-system reasoning
C. It makes authentication unnecessary
D. It converts all dynamic queries into static prompts

**Answer:** B
**Explanation:** Exposing reference content as resources helps the model understand system structure before invoking tools, which improves efficiency and reduces unnecessary discovery calls. A is too absolute, C is unrelated, and D misunderstands resources as replacing all dynamic behavior.

### Q4. Which scenario is the **best** use of an MCP tool rather than a resource?

A. Publishing a static data dictionary used in many workflows
B. Exposing an API reference manual for read-only inspection
C. Submitting a purchase order that creates a real transaction in an ERP system
D. Providing a glossary of internal abbreviations

**Answer:** C
**Explanation:** Creating a purchase order is an action with side effects, making it a strong fit for a tool. The other options are stable reference material that is better represented as resources to avoid needless invocation overhead.

### Q5. An engineer wants an MCP server to be available only inside one repository so that other projects do not see it. Which scope is most appropriate?

A. Global host scope
B. User scope
C. Project scope
D. Session scope only

**Answer:** C
**Explanation:** **Project scope** is intended for repository-specific or application-specific server configuration. User scope would make it broadly available across projects, and the other options are either too vague or not the standard scope choice being tested.

### Q6. Which configuration approach is most appropriate for handling MCP server credentials in a shared codebase?

A. Hard-code API keys in the server configuration for reproducibility
B. Store secrets in plaintext inside a project README
C. Use environment variable expansion so the configuration references values supplied securely outside the config file
D. Add credentials to tool descriptions so the model knows when to use them

**Answer:** C
**Explanation:** Environment variable expansion is the standard pattern because it keeps secrets out of versioned configuration while still allowing deterministic setup. A and B expose secrets, and D is both insecure and conceptually wrong because descriptions are not a credential store.

### Q7. After configuring a new MCP server, what is the most reliable next step to confirm the integration is functioning?

A. Assume the server is available if the config file parses
B. Verify that the host discovers the server's tools/resources and that they appear as expected
C. Immediately force tool usage in production tasks
D. Restart the model weights

**Answer:** B
**Explanation:** Successful integration requires more than syntax validity; the host or client must actually discover and expose the server's capabilities. A is insufficient, C skips validation, and D is nonsensical because model weights are unrelated to MCP configuration.

### Q8. Which tool description is **best** for reducing tool misrouting?

A. "Searches stuff. Use when needed."
B. "General data tool for any account, invoice, or user action."
C. "Look up customer records by customer ID or exact email. Read-only. Do not use for invoice lookup or account updates; use `billing_get_invoice` or `crm_update_customer` instead."
D. "Customer helper tool. Flexible inputs."

**Answer:** C
**Explanation:** Good MCP tool descriptions clearly state purpose, input format, boundaries, and nearby alternatives. A, B, and D are vague and increase the chance the model picks the wrong tool or passes malformed inputs.

### Q9. Why is it useful to mention semantically similar tools in a tool's description?

A. It increases token usage, which improves tool quality
B. It helps the model disambiguate adjacent capabilities and choose the correct tool
C. It prevents the tool from needing authentication
D. It forces the host to rank that tool first

**Answer:** B
**Explanation:** Cross-referencing similar tools reduces ambiguity, especially when names are related or workflows span adjacent systems. A is not a benefit by itself, C is unrelated, and D confuses description text with host-side ranking behavior.

### Q10. You need Claude to return a validated record created by an external system, and plain natural-language output is not acceptable. Which configuration is most appropriate?

A. Leave tool selection entirely automatic and hope the model calls the tool
B. Disable all tools so the model produces a concise answer
C. Use `tool_choice` to require the needed tool invocation
D. Convert the tool into a resource

**Answer:** C
**Explanation:** When structured output depends on a tool being called, `tool_choice` should be used to guarantee invocation rather than relying on model discretion. A is unreliable, B prevents the required action, and D would remove the action semantics needed to create or retrieve the result.

### Q11. A workflow needs: (1) resolve a customer by email, then (2) fetch open invoices using the resulting customer ID. What is the best design pattern?

A. Call both tools in parallel to reduce latency
B. First call the resolver tool, then use its output as input to the invoice tool
C. Skip the resolver and let the invoice tool infer the ID from context
D. Use only resources, because tools should never depend on each other

**Answer:** B
**Explanation:** This is a dependency chain: the second tool requires data from the first, so sequencing is necessary. A risks missing required inputs, C assumes unsupported behavior, and D falsely suggests multi-tool workflows are undesirable.

### Q12. Which statement about MCP transports is most accurate?

A. `stdio` is commonly used for local process integration, while HTTP/SSE is useful for remotely reachable or service-style MCP servers
B. `stdio` is only for browser applications, while HTTP/SSE is only for desktop apps
C. HTTP/SSE cannot support tool invocation
D. Transport choice has no effect on deployment architecture

**Answer:** A
**Explanation:** `stdio` fits local subprocess-style integrations well, while HTTP/SSE is commonly used for network-accessible servers or service deployments. B and C are false, and D ignores operational realities like process boundaries, hosting, and connectivity.

### Q13. Which naming scheme best supports MCP tool clarity in a multi-domain environment?

A. `run`, `search`, `update`
B. `tool1`, `tool2`, `tool3`
C. `crm_lookup_customer`, `billing_get_invoice`, `calendar_create_event`
D. `customer`, `invoice`, `calendar`

**Answer:** C
**Explanation:** Namespaced, domain-prefixed tool names make purpose and ownership much clearer, especially when many servers or domains coexist. The other choices are overly generic and increase ambiguity during tool selection.

### Q14. A server exposes thousands of product documents. Which design is most likely to improve agent efficiency?

A. Force the model to discover each document by repeated search tools only
B. Expose stable catalogs or indexes as resources, then use tools for targeted actions or dynamic lookups
C. Put every document directly into one tool description
D. Avoid resources because they compete with tools

**Answer:** B
**Explanation:** A resource-based catalog gives the model orientation and reduces wasteful exploration, while tools remain available for live operations and filtered retrieval. A is inefficient, C is impractical, and D misunderstands resources and tools as competing rather than complementary.

### Q15. Which authentication pattern is **least** appropriate for MCP integration in enterprise environments?

A. Environment variables supplied by the runtime or shell
B. Secret injection through deployment configuration
C. Storing long-lived credentials directly in version-controlled server config
D. Using per-environment credential values with the same config template

**Answer:** C
**Explanation:** Secrets should not be committed to source control because that creates major leakage and rotation problems. A, B, and D are all aligned with safer operational practices that separate config structure from secret values.

### Q16. A tool accepts only a JSON object with fields `{ "ticket_id": string, "priority": "low|medium|high" }`. What should its description include?

A. Only a marketing-style summary so the model is not overwhelmed
B. Clear input format expectations, allowed values, and when not to use the tool
C. No input details; the model can infer the schema from the name
D. A list of internal implementation classes

**Answer:** B
**Explanation:** Explicit schema expectations reduce malformed calls and improve routing accuracy. A and C hide critical usage information, while D is implementation detail that rarely helps correct invocation.

### Q17. Which scenario most strongly justifies using `tool_choice` to force a specific tool?

A. When the answer can be safely composed from already available context
B. When a compliance workflow requires an auditable lookup from a system of record before answering
C. When you want the model to be more creative
D. When you are unsure whether the tool works

**Answer:** B
**Explanation:** If the answer must come from a verified external action or lookup, forcing the tool ensures the required evidence path is followed. A does not require forced invocation, C is unrelated, and D indicates a testing problem rather than a tool-choice strategy.

### Q18. Which statement about resources vs tools in cross-system queries is **most** correct?

A. Resources are mainly useful for background colors and UI styling, while tools do the real work
B. Resources can provide schemas, catalogs, and reference context that help the model plan cross-system tool usage more intelligently
C. Tools should always be called before resources so the model has fresh outputs
D. Resources eliminate the need for tool descriptions

**Answer:** B
**Explanation:** In cross-system scenarios, resources can expose the structural context—such as schemas, IDs, mappings, and glossaries—that lets the model choose and sequence tools more effectively. A is irrelevant, C is too rigid, and D is false because tools still need precise descriptions even when good resources exist.

### Q19. A developer installs an MCP server at user scope, but a project requires a different version and configuration of the same server. What is the best interpretation?

A. User scope always overrides project scope
B. Project scope exists specifically to support repository-specific behavior without changing the user-wide default
C. MCP does not support multiple configurations for the same capability area
D. The server must be rewritten to use HTTP/SSE

**Answer:** B
**Explanation:** Project scope is intended for per-repository customization, allowing a project to define its own server behavior independent of broader defaults. A is too absolute, C is incorrect, and D confuses scope management with transport selection.

### Q20. Which tool pair is **most** in need of explicit boundary language in their descriptions?

A. `weather_get_forecast` and `erp_submit_purchase_order`
B. `crm_search_customer` and `crm_get_customer_by_id`
C. `calendar_create_event` and `filesystem_read_file`
D. `math_add` and `teams_send_message`

**Answer:** B
**Explanation:** These two tools are semantically close, so the model needs help distinguishing when to search by approximate criteria versus fetch by exact identifier. The other pairs are already distinct enough that misrouting is less likely even with shorter descriptions.

---

[← Previous: Structured Outputs](04-structured-outputs-and-review-design.md) · [Back to index](../README.md)
