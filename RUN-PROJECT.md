# Running the Cybersecurity Fatigue Research System

This guide shows you how to run the completed multi-agent research system you built in the tutorial.

## Prerequisites

Before running this project, ensure you've completed:

1. ✅ Installed Python 3.11+
2. ✅ Installed Claude Code
3. ✅ Downloaded the three research papers to `papers/` folder
4. ✅ Created the project structure (`.claude/skills/`, `scripts/tools/`, etc.)
5. ✅ Configured the MCP server in `.claude/mcp_settings.json`
6. ✅ Updated `.claude/settings.json` with code execution and skills enabled

## Step 1: Install Python Dependencies

Open your terminal and navigate to the project folder.

### macOS/Linux:

```bash
cd ~/Documents/cyber-fatigue-research
pip3 install -r requirements.txt
```

### Windows:

```bash
cd %USERPROFILE%\Documents\cyber-fatigue-research
pip install -r requirements.txt
```

**What this does:** Installs PyPDF2 (for reading PDFs), scipy and numpy (for statistical analysis).

**Expected output:** You should see messages like "Successfully installed PyPDF2-3.0.1 scipy-1.11.4 numpy-1.26.2"

---

## Step 2: Verify Your Setup

Before running the full workflow, check that everything is configured correctly.

### Check that Claude Code is installed:

```bash
claude --version
```

You should see something like `2.0.21 (Claude Code)` or similar.

### Verify your project structure:

```bash
ls -la
```

**On Windows, use:**

```bash
dir
```

You should see:
- `.claude/` folder
- `papers/` folder (with 3 PDF files)
- `scripts/` folder
- `results/` folder (empty except for `.gitkeep`)
- `requirements.txt`
- `CLAUDE.md`

### Verify the MCP configuration:

**macOS/Linux:**

```bash
cat .claude/mcp_settings.json
```

**Windows:**

```bash
type .claude\mcp_settings.json
```

Make sure the path points to YOUR actual papers folder location (not someone else's computer path).

---

## Step 3: Launch Claude Code

Now you're ready to start Claude Code and run the orchestrator.

### Start Claude Code:

```bash
claude
```

This opens the Claude Code interface in your terminal.

**What you'll see:** A welcome message and a prompt where you can type commands.

---

## Step 4: Run the Research Orchestrator

Once Claude Code is running, invoke the orchestrator skill to execute the full workflow.

### Type this command:

```
Using the research-orchestrator skill, analyze the three papers in the papers/ folder to investigate how years of professional experience relates to cybersecurity fatigue. Complete the full workflow: 1. Extract data from all papers 2. Calculate overall correlation 3. Write a professional article 4. Have the antagonist review it
```

**What happens:**

1. Claude Code loads the `research-orchestrator` skill
2. The orchestrator delegates to the `academic-researcher` skill to extract data from PDFs
3. The researcher creates `results/parsed_papers.json`
4. The researcher calculates statistics and creates `results/correlation_analysis.json`
5. The orchestrator invokes the `technical-copywriter` skill to write the article
6. The copywriter creates `results/draft_article.md`
7. The orchestrator invokes the `research-antagonist` skill to review
8. The antagonist creates `results/review_feedback.json`
9. If revisions are needed, the copywriter is invoked again
10. Once approved, the workflow completes

**Time estimate:** 10-15 minutes for the complete workflow

---

## Step 5: View Your Results

After the workflow completes, check the `results/` folder for your outputs.

### macOS/Linux:

```bash
ls -la results/
```

### Windows:

```bash
dir results\
```

You should now see:
- `parsed_papers.json` - Structured data from all three papers
- `correlation_analysis.json` - Statistical analysis results
- `draft_article.md` - Publication-ready article (1,200+ words)
- `review_feedback.json` - Quality review with status "APPROVED"

### Read the final article:

**macOS/Linux:**

```bash
cat results/draft_article.md
```

**Windows:**

```bash
type results\draft_article.md
```

Or open it in any text editor.

---

## Troubleshooting Common Issues

### Issue 1: "Skills not found" error

**Problem:** Claude Code says it can't find the `research-orchestrator` skill.

**Fix:**
1. Make sure your skills are in `.claude/skills/` (NOT just `skills/`)
2. Restart Claude Code: type `exit` then `claude` again
3. Verify skill files exist:
   ```bash
   ls .claude/skills/orchestrator/SKILL.md
   ls .claude/skills/researcher/SKILL.md
   ls .claude/skills/copywriter/SKILL.md
   ls .claude/skills/antagonist/SKILL.md
   ```

### Issue 2: "Cannot read PDF" error

**Problem:** The researcher skill says it can't find the papers.

**Fix:**
1. Check your MCP configuration path in `.claude/mcp_settings.json`
2. Make sure the path uses forward slashes even on Windows: `C:/Users/YourName/...` not `C:\Users\...`
3. Update the path to YOUR actual location:
   ```json
   {
     "mcpServers": {
       "filesystem": {
         "command": "npx",
         "args": ["-y", "@modelcontextprotocol/server-filesystem", "/ABSOLUTE/PATH/TO/YOUR/papers"],
         "description": "Provides read-only access to research papers"
       }
     }
   }
   ```
4. Restart Claude Code

### Issue 3: Python import errors

**Problem:** Error messages about PyPDF2, scipy, or numpy not found.

**Fix:**
1. Make sure you installed requirements: `pip install -r requirements.txt`
2. Check your Python version: `python --version` (should be 3.11+)
3. Try using `pip3` instead of `pip`:
   ```bash
   pip3 install -r requirements.txt
   ```

### Issue 4: "code_execution": false error

**Problem:** Claude says it can't run Python code.

**Fix:**
1. Open `.claude/settings.json`
2. Make sure it includes:
   ```json
   {
     "code_execution": {
       "enabled": true,
       "timeout": 300
     },
     "skills": {
       "enabled": true,
       "auto_invoke": true
     }
   }
   ```
3. Restart Claude Code

### Issue 5: Empty results/ folder after workflow

**Problem:** The workflow seems to complete but no files are created.

**Fix:**
1. Check the antagonist review: Did it find issues requiring revision?
2. Look for error messages in Claude's output
3. Try running each stage manually:
   ```
   Using the academic-researcher skill, extract data from papers in the papers/ folder
   ```
4. Check file permissions on the `results/` folder

---

## Running Individual Stages

If you want to run just one part of the workflow instead of the full pipeline:

### Extract data only:

```
Using the academic-researcher skill, extract data from the papers in the papers/ folder and save to results/parsed_papers.json
```

### Calculate statistics only (requires parsed data):

```
Using the academic-researcher skill, calculate correlation statistics from results/parsed_papers.json
```

### Write article only (requires statistics):

```
Using the technical-copywriter skill, write an article from the data in results/correlation_analysis.json
```

### Review article only (requires draft):

```
Using the research-antagonist skill, review the article in results/draft_article.md
```

---

## Comparing Your Output to Examples

After your workflow completes, compare your results to the expected output:

```bash
# Compare your parsed data structure
diff results/parsed_papers.json examples/expected-output/parsed_papers.json

# Compare your article (content will differ but structure should match)
wc -w results/draft_article.md
wc -w examples/expected-output/draft_article.md
```

The word counts should be similar (within 10-20%), and your review should also show "APPROVED" status.

---

## Next Steps

Once you've successfully run the workflow:

1. **Experiment with different papers:** Replace the PDFs in `papers/` with other research papers on cybersecurity fatigue
2. **Modify the skills:** Edit `.claude/skills/*/SKILL.md` files to change how agents behave
3. **Add new agents:** Create a new skill in `.claude/skills/your-skill-name/SKILL.md`
4. **Customize the output:** Modify the copywriter instructions to change article style
5. **Make the antagonist stricter:** Add more quality checks to `.claude/skills/antagonist/SKILL.md`

---

## Getting Help

If you run into issues:

1. Check the [tutorial](link-to-your-tutorial) for detailed setup steps
2. Read `CLAUDE.md` for project-specific information
3. Verify all paths are absolute (not relative) in your MCP config
4. Make sure you're in the correct directory when running commands
5. Try `claude --help` for Claude Code command options

---

## What You Just Built

Congratulations! You've successfully run a multi-agent AI research system that:

✅ Reads academic PDFs automatically
✅ Extracts structured data (metadata, statistics, findings)
✅ Performs statistical analysis (correlations, effect sizes)
✅ Writes professional articles with proper citations
✅ Reviews its own work for quality issues
✅ Revises based on feedback until approved

This same pattern can be applied to any domain that requires coordination between specialist agents: data analysis, content creation, code review, report generation, and more.
