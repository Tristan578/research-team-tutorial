# Multi-Agent Research System Tutorial

**Learn to build a multi-agent AI research system using Claude Code that reads academic papers, performs statistical analysis, writes professional articles, and reviews its own work.**

![Project Status](https://img.shields.io/badge/status-tutorial-blue)
![Claude Code](https://img.shields.io/badge/Claude%20Code-2.0+-purple)
![Python](https://img.shields.io/badge/python-3.11+-green)

## What You'll Build

This tutorial teaches you to create a coordinated team of AI agents that:

- **Extracts data** from academic PDFs automatically
- **Calculates statistics** (correlations, effect sizes, regression models)
- **Writes professional articles** with proper citations and statistical reporting
- **Reviews and revises** outputs until quality standards are met
- **Coordinates workflow** between specialized agents

## Why This Matters

Multi-agent systems represent a powerful paradigm for complex tasks that require:
- Domain expertise across different areas
- Quality control and error checking
- Iterative refinement based on feedback
- Reproducible research workflows

This tutorial demonstrates these concepts through a real research task: analyzing the relationship between professional experience and cybersecurity fatigue across three academic papers.

## What You'll Learn

### Core Concepts
- **Claude Code Skills**: Create AI agents with specialized capabilities
- **Agent Orchestration**: Coordinate multiple agents in a workflow
- **Model Context Protocol (MCP)**: Securely access external resources
- **Python Integration**: Execute code for data processing and statistics
- **Quality Control Loops**: Implement review and revision cycles

### Technical Skills
- Writing skill definitions with YAML frontmatter
- Delegating tasks between agents using the Skill tool
- Configuring MCP servers for file access
- Running Python scripts via Claude Code's Bash tool
- Implementing validation checkpoints

## Prerequisites

### Required
- **Claude Code 2.0+** - [Install here](https://claude.com/claude-code)
- **Python 3.11+** - [Download Python](https://www.python.org/downloads/)
- **Basic terminal knowledge** - Ability to run commands and navigate directories
- **Text editor** - VS Code, Sublime, or any plain text editor

### Helpful (but not required)
- Familiarity with YAML syntax
- Understanding of academic research papers
- Basic statistics knowledge (correlation, p-values)

## Project Structure

```
cyber-fatigue-research/
├── .claude/
│   ├── skills/                    # AI agent definitions
│   │   ├── orchestrator/
│   │   │   └── SKILL.md          # Coordinates the workflow
│   │   ├── researcher/
│   │   │   └── SKILL.md          # Extracts data and calculates stats
│   │   ├── copywriter/
│   │   │   └── SKILL.md          # Writes professional articles
│   │   └── antagonist/
│   │       └── SKILL.md          # Reviews for quality issues
│   ├── mcp_settings.json.template # MCP configuration template
│   └── settings.json              # Claude Code settings
├── papers/                        # Research papers (you provide these)
│   └── .gitkeep
├── scripts/
│   └── tools/
│       └── research_tools.py      # Python utilities for PDF and stats
├── results/                       # Generated outputs
│   └── .gitkeep
├── examples/
│   └── expected-output/           # Reference outputs from successful run
│       ├── parsed_papers.json
│       ├── correlation_analysis.json
│       ├── draft_article.md
│       ├── review_feedback.json
│       └── README.md
├── CLAUDE.md                      # Guide for Claude Code instances
├── RUN-PROJECT.md                 # Step-by-step execution guide
├── revisions.md                   # Tutorial improvement recommendations
├── requirements.txt               # Python dependencies
└── README.md                      # This file
```

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/Tristan578/research-team-tutorial.git
cd research-team-tutorial
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

**What this installs:**
- `PyPDF2` - PDF text extraction
- `scipy` - Statistical calculations
- `numpy` - Numerical operations

### 3. Configure MCP Server

Copy the template and update with your local path:

```bash
# Copy template
cp .claude/mcp_settings.json.template .claude/mcp_settings.json

# Edit .claude/mcp_settings.json and replace:
# "ABSOLUTE_PATH_TO_YOUR_PAPERS_FOLDER"
# with your actual absolute path, e.g.:
# "/Users/yourname/Documents/research-team-tutorial/papers"
```

**Important:** Use forward slashes even on Windows: `C:/Users/yourname/...`

### 4. Download Research Papers

You'll need these three papers (not included due to copyright):

1. **Stanton et al. (2016)** - "Security Fatigue" - *IT Professional*
2. **Reeves et al. (2021)** - "The Effect of Cybersecurity Professional's Job Satisfaction and Burnout on Safeguarding Organizational Data Security" - *Frontiers in Psychology*
3. **Mizrak et al. (2025)** - "Examining the factors affecting security fatigue in a multinational sample: A new theoretical perspective" - *Computers & Security*

Download these papers and place them in the `papers/` folder.

### 5. Run the System

```bash
# Launch Claude Code
claude

# In Claude Code, run:
Using the research-orchestrator skill, analyze the three papers in the papers/ folder to investigate how years of professional experience relates to cybersecurity fatigue. Complete the full workflow: 1. Extract data from all papers 2. Calculate overall correlation 3. Write a professional article 4. Have the antagonist review it
```

**Expected time:** 10-15 minutes

### 6. View Results

Check the `results/` folder for:
- `parsed_papers.json` - Structured data from papers
- `correlation_analysis.json` - Statistical analysis
- `draft_article.md` - Professional article (1,200+ words)
- `review_feedback.json` - Quality review with approval status

Compare your outputs with `examples/expected-output/` to verify success.

## Tutorial Files

This repository includes comprehensive documentation:

- **[RUN-PROJECT.md](RUN-PROJECT.md)** - Detailed execution guide for beginners
  - Step-by-step instructions
  - Platform-specific commands (macOS/Linux/Windows)
  - Troubleshooting for 5 common issues
  - Individual stage execution

- **[CLAUDE.md](CLAUDE.md)** - Reference for Claude Code instances
  - Project architecture
  - Multi-agent workflow
  - Data flow diagrams
  - Statistical reporting requirements

- **[revisions.md](revisions.md)** - Tutorial improvement recommendations
  - 12 comprehensive revisions
  - Implementation priority guide
  - Testing strategies
  - Success metrics

## How It Works

### Multi-Agent Workflow

```
┌─────────────────────────────────────────────────────────┐
│                    ORCHESTRATOR                         │
│         (Coordinates overall workflow)                  │
└─────────────────────────────────────────────────────────┘
                          │
        ┌─────────────────┼─────────────────┐
        ▼                 ▼                 ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│  RESEARCHER  │  │  COPYWRITER  │  │  ANTAGONIST  │
│              │  │              │  │              │
│ Extracts &   │  │ Writes       │  │ Reviews &    │
│ Analyzes     │──▶│ Article      │──▶│ Critiques    │
│ Papers       │  │              │  │              │
└──────────────┘  └──────────────┘  └──────────────┘
                          │                 │
                          └────────┬────────┘
                                   ▼
                            ┌─────────────┐
                            │  Revision   │
                            │  Loop if    │
                            │  Needed     │
                            └─────────────┘
```

### Stage-by-Stage Breakdown

**Stage 1: Data Extraction**
- Orchestrator delegates to Researcher
- Researcher reads PDFs using MCP filesystem server
- Python `extract_pdf_text()` extracts text
- Structured JSON created with metadata, methods, statistics, findings

**Stage 2: Statistical Analysis**
- Orchestrator delegates to Researcher again
- Python `calculate_correlation()` computes statistics
- Fisher z-transformation for meta-analysis
- Results saved to `correlation_analysis.json`

**Stage 3: Article Writing**
- Orchestrator delegates to Copywriter
- Copywriter reads correlation analysis
- Writes 1,200+ word article with:
  - Professional tone for business/tech audiences
  - Proper statistical reporting (r, n, p-values)
  - Full citations for all three papers
  - Practical implications

**Stage 4: Quality Review**
- Orchestrator delegates to Antagonist
- Antagonist reviews for:
  - Statistical accuracy
  - Methodological rigor
  - Causal language errors
  - Citation formatting
  - Clarity and coherence
- Returns APPROVED or REVISION_REQUIRED with detailed feedback

**Stage 5: Revision (if needed)**
- If revision required, Orchestrator sends Copywriter back to Stage 3
- Loop continues until Antagonist approves

## Skills System

Each agent is defined by a `SKILL.md` file with YAML frontmatter:

```yaml
---
name: research-orchestrator
description: Coordinates academic research workflow
allowed-tools: [Skill, Task, Read, Write, TodoWrite]
---

# Research Orchestrator

You manage research projects from start to finish...
```

**Key components:**
- `name` - Unique identifier for the skill
- `description` - What the skill does
- `allowed-tools` - Which Claude Code tools this agent can use
- Markdown body - Detailed instructions and examples

## Model Context Protocol (MCP)

MCP provides secure, controlled access to external resources:

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/absolute/path/to/papers"
      ],
      "description": "Provides read-only access to research papers"
    }
  }
}
```

**Why MCP?**
- Security: Read-only access to specific directories
- Isolation: Skills can't access arbitrary files
- Transparency: Users control what resources agents can access

## Python Integration

Claude Code executes Python via the Bash tool:

```python
# scripts/tools/research_tools.py

def calculate_correlation(experience_data, fatigue_data):
    """Calculate Pearson correlation with confidence interval."""
    from scipy import stats
    import numpy as np

    r, p_value = stats.pearsonr(experience_data, fatigue_data)
    n = len(experience_data)

    # Fisher z-transformation for confidence interval
    z = np.arctanh(r)
    se = 1 / np.sqrt(n - 3)
    ci_lower = np.tanh(z - 1.96 * se)
    ci_upper = np.tanh(z + 1.96 * se)

    return {
        "r": round(r, 3),
        "p_value": p_value,
        "n": n,
        "ci_95": [round(ci_lower, 3), round(ci_upper, 3)]
    }
```

Claude Code can:
- Execute Python scripts
- Capture output (stdout/stderr)
- Parse JSON results
- Handle errors and exceptions

## Customization

### Change the Research Question

Edit the orchestrator prompt to analyze different relationships:

```
Using the research-orchestrator skill, analyze how organizational size
relates to security awareness training effectiveness...
```

### Add New Agent Types

Create a new skill directory:

```bash
mkdir -p .claude/skills/data-visualizer
touch .claude/skills/data-visualizer/SKILL.md
```

Define the agent:

```yaml
---
name: data-visualizer
description: Creates charts and graphs from statistical data
allowed-tools: [Read, Write, Bash]
---

# Data Visualizer

You create professional visualizations...
```

Invoke from orchestrator:

```
Use Skill tool with command: "data-visualizer"
```

### Modify Quality Standards

Edit `.claude/skills/antagonist/SKILL.md` to add stricter checks:

```markdown
## Critical Issues (block approval):
- Statistical reporting errors
- Causal language for correlational data
- Missing confidence intervals
- Sample size not reported
- Effect sizes missing
- NEW: Missing power analysis
- NEW: Unreported effect size interpretations
```

## Troubleshooting

### Skills not found
- Ensure skills are in `.claude/skills/` not `skills/`
- Restart Claude Code
- Check file names are exactly `SKILL.md`

### Cannot read PDFs
- Verify MCP path in `.claude/mcp_settings.json`
- Use absolute paths with forward slashes
- Restart Claude Code after config changes

### Python import errors
- Run `pip install -r requirements.txt`
- Check Python version: `python --version` (need 3.11+)
- Use `pip3` instead of `pip` if needed

### Empty results folder
- Check antagonist review - revisions may be required
- Look for error messages in Claude's output
- Verify file permissions on `results/` directory

See [RUN-PROJECT.md](RUN-PROJECT.md) for detailed troubleshooting.

## Contributing

This is a tutorial project. If you find issues or have improvements:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

See [revisions.md](revisions.md) for planned improvements.

## License

MIT License - See LICENSE file for details

**Note:** Research papers are not included due to copyright. Users must download papers separately.

## Acknowledgments

- **Anthropic** for Claude Code and the Model Context Protocol
- **Research authors** for the cybersecurity fatigue studies
- **PyPDF2, SciPy, NumPy** maintainers for excellent open-source tools

## Learn More

- [Claude Code Documentation](https://docs.claude.com/claude-code)
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [Skills Documentation](https://docs.claude.com/claude-code/skills)

## Support

Questions or issues?
- Check [RUN-PROJECT.md](RUN-PROJECT.md) for execution help
- Open an issue on GitHub

---

**Built with Claude Code** - Teaching AI agents to collaborate on complex research tasks.
