# Objective 32: Built-in Tool Selection

[← Back to objectives index](README.md) · [Back to main index](../../README.md)

> **Exam objective:** Select the appropriate Claude Code built-in tool—Grep, Glob, Read, or Bash—based on the nature of the search or file operation required for a given codebase task.

---

### Q1.
You need to find every TypeScript file whose name ends with `AuthService.ts` anywhere in a large repository before inspecting them. Which built-in tool is the best first choice?

A. Read
B. Bash
C. Glob
D. Grep

**Answer:** C
**Explanation:** Glob is designed for filename and path-pattern matching, making it the fastest fit for locating files by name. Grep searches file contents, Read requires already knowing the file path, and Bash would be a less targeted fallback.

### Q2.
An engineer asks you to locate every usage of the string `dangerouslySetInnerHTML` across React components. Which tool is most appropriate?

A. Grep
B. Glob
C. Read
D. Bash

**Answer:** A
**Explanation:** Grep is the right tool for content-based search across files when you know the token or pattern to find. Glob only finds filenames, Read inspects known files, and Bash is unnecessary for a straightforward text search.

### Q3.
You already know the exact path `src\api\routes\payments.ts` and need to inspect the implementation around a specific handler. Which tool should you use first?

A. Glob
B. Read
C. Grep
D. Bash

**Answer:** B
**Explanation:** Read is ideal when the file path is known and the goal is to inspect file contents directly. Grep and Glob are discovery tools, while Bash is broader than needed for simple file reading.

### Q4.
You must list the top-level folders in a repository and then run an existing test command defined by the project. Which built-in tool is best for actually executing the test command?

A. Read
B. Grep
C. Bash
D. Glob

**Answer:** C
**Explanation:** Bash is appropriate when you need to execute shell commands such as the project's test runner. The other tools are optimized for searching or reading, not command execution.

### Q5.
You need all Markdown files under `docs\` whose filenames contain `migration`, but you do not care about their contents yet. Which tool is best?

A. Glob
B. Grep
C. Read
D. Bash

**Answer:** A
**Explanation:** This is a path-matching problem, so Glob is the right choice. Grep would search inside files, Read needs exact files already identified, and Bash is a less specialized fallback.

### Q6.
You suspect a function named `buildSessionContext` is defined in one file and called in several others. What is the best first tool?

A. Bash
B. Read
C. Grep
D. Glob

**Answer:** C
**Explanation:** Grep can quickly locate the function definition and references by searching content across the codebase. Glob only narrows by filenames, and Read is best after the relevant files are known.

### Q7.
You have already used Grep to find three candidate files and now need to compare the surrounding code in each file. Which next step is best?

A. Use Read on those specific files
B. Use Glob again on the same directory
C. Use Bash to print the whole repository
D. Use Grep with a broader pattern

**Answer:** A
**Explanation:** Once candidate files are identified, Read is the most direct tool for detailed inspection. Re-running discovery tools or dumping overly broad output adds noise instead of progressing the task.

### Q8.
Which scenario most strongly justifies choosing Bash over Grep, Glob, and Read?

A. You need to search for `TODO` comments in Python files
B. You know the exact file path and want to inspect 30 lines
C. You need to run `npm test` and capture the resulting failures
D. You need to find all files named `config.yaml`

**Answer:** C
**Explanation:** Bash is the correct choice when the task requires command execution, such as running a test suite. The other scenarios map directly to Grep, Read, and Glob respectively.

### Q9.
You need to identify files whose names match `*Controller*.cs` and then search only those files for `Authorize(`. What is the most efficient tool sequence?

A. Read, then Bash
B. Glob, then Grep scoped to the matched files
C. Grep the entire repo, then Glob
D. Bash only

**Answer:** B
**Explanation:** First use Glob to narrow the candidate set by filename, then Grep within that scoped set for the code pattern. This reduces unnecessary scanning and aligns each tool to its intended strength.

### Q10.
An agent uses Bash to run a shell command just to open a known file and print its contents. Why is that usually suboptimal?

A. Bash cannot read files
B. Read is a more specialized and lower-overhead tool for inspecting known files
C. Glob would always be faster
D. Grep can replace all Bash operations

**Answer:** B
**Explanation:** Read is purpose-built for viewing known files, making it more direct and typically less noisy than a shell command. Bash can do it, but using the simplest correct built-in tool reduces complexity and error surface.

### Q11.
You need to know whether a repo contains any file named `Dockerfile.prod` before doing anything else. Which tool is most appropriate?

A. Glob
B. Read
C. Grep
D. Bash

**Answer:** A
**Explanation:** The question is about file existence by name and location, which is exactly what Glob handles well. Grep searches contents, Read assumes a known path, and Bash is unnecessary for a simple file-pattern lookup.

### Q12.
You are investigating whether a config value `max_request_bytes` appears anywhere in YAML or TOML files. Which tool is the best first choice?

A. Grep
B. Glob
C. Read
D. Bash

**Answer:** A
**Explanation:** Because you are searching for a content string across files, Grep is the right starting tool. You can optionally scope it by file type, but the core need is text search rather than filename discovery.

### Q13.
A teammate says, "Glob can replace Grep because both are just search tools." Which response is most accurate?

A. Correct; the distinction is mostly historical
B. Incorrect; Glob searches paths and filenames, while Grep searches file contents
C. Incorrect; Glob executes commands and Grep reads files
D. Correct only in Bash mode

**Answer:** B
**Explanation:** The key distinction is what is being searched: path patterns versus file contents. Treating them as interchangeable often leads to inefficient or incorrect tool choices.

### Q14.
You know a failing test mentions `payments retry window`, but you do not know which file contains that text. Which tool should you start with?

A. Read
B. Glob
C. Grep
D. Bash

**Answer:** C
**Explanation:** Since the file is unknown and the search target is text, Grep is the correct starting point. Read requires a path, Glob searches names rather than content, and Bash is broader than needed.

### Q15.
In a codebase task, which principle best summarizes correct tool selection among Grep, Glob, Read, and Bash?

A. Always use Bash first because it is the most flexible
B. Prefer the narrowest built-in tool that directly matches the task: filename search, content search, file inspection, or command execution
C. Use Read for all tasks once you know the repository root
D. Use Grep whenever performance matters, regardless of task type

**Answer:** B
**Explanation:** Efficient tool selection means using the most specialized tool that fits the job, which reduces noise and unnecessary decision-making. The other options overgeneralize one tool beyond its intended purpose.

---

[← Back to objectives index](README.md) · [Back to main index](../../README.md)
