# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a multi-agent research project focused on analyzing cybersecurity fatigue through systematic literature review. The project uses Claude Code's skill system to orchestrate specialized agents that extract data from research papers, perform statistical analysis, write technical articles, and review outputs for quality.

## Architecture

### Multi-Agent Workflow

The project uses a skill-based architecture with four specialized agents:

1. **Orchestrator** (`.claude/skills/orchestrator/SKILL.md`) - Coordinates the entire research pipeline
2. **Researcher** (`.claude/skills/researcher/SKILL.md`) - Extracts data from PDF papers and performs correlation analysis
3. **Copywriter** (`.claude/skills/copywriter/SKILL.md`) - Transforms research findings into professional articles
4. **Antagonist** (`.claude/skills/antagonist/SKILL.md`) - Quality control reviewer that validates outputs

### Data Flow

```
papers/ (PDFs)
  → Researcher extracts data
  → results/parsed_papers.json
  → Researcher performs correlation analysis
  → results/correlation_analysis.json
  → Copywriter writes article
  → results/draft_article.md
  → Antagonist reviews
  → results/review_feedback.json
```

### Directory Structure

- `papers/` - Source research papers (PDFs) for analysis
- `.claude/skills/` - Claude Code skill definitions for specialized agents
- `scripts/tools/` - Python utilities for PDF extraction and statistical analysis
- `results/` - Generated outputs (JSON data files, markdown articles, reviews)
- `.claude/mcp_settings.json` - MCP server configuration for filesystem access

## MCP Configuration

The project uses the Model Context Protocol (MCP) filesystem server to provide read-only access to research papers:

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "D:/repos/claude-code-agents/cyber-fatigue-research/papers"],
      "description": "Provides read-only access to research papers"
    }
  }
}
```

**Important**: The filesystem path is hardcoded to an absolute Windows path. Update this if the repository is moved or cloned to a different location.

## Working with Skills

### Invoking Skills

Use the Skill tool to invoke specialized agents:
- `research-orchestrator` - Start the full research pipeline
- `academic-researcher` - Extract data from papers and calculate correlations
- `technical-copywriter` - Generate article from analysis results
- `research-antagonist` - Review draft article for quality issues

### Skill Inputs and Outputs

**Copywriter** expects:
- Input: `results/correlation_analysis.json`, `results/parsed_papers.json`
- Output: `results/draft_article.md`

**Antagonist** expects:
- Input: `results/draft_article.md`
- Output: `results/review_feedback.json` with status "APPROVED" or "REVISION_REQUIRED"

## Statistical Reporting Requirements

When working with research data, follow these strict guidelines:

**Always include four pieces for correlations:**
- Correlation coefficient (r = X.XX)
- Sample size (n = XXX)
- P-value (p < X.XX)
- Confidence interval (95% CI [X.XX, X.XX])

**Example**: "Experience correlated positively with fatigue (r = 0.38, n = 847, p < 0.001, 95% CI [0.28, 0.47])."

**Never claim causation from correlational data:**
- Bad: "Experience causes fatigue"
- Good: "Experience correlates with fatigue"

**Effect size interpretation:**
- r < 0.3 = small/weak
- r = 0.3 to 0.5 = moderate
- r > 0.5 = strong

## Writing Standards

When generating or reviewing articles:
- Professional but accessible tone (no academic jargon)
- Evidence-based (every claim needs data)
- Direct and clear (short sentences, active voice)
- No marketing hype (avoid "groundbreaking," "revolutionary")
- Technical terms must be defined on first use
- All papers must be cited by author and year

## Current Papers in Analysis

- `stanton-et-al-2016-security-fatigue.pdf` (1.6 MB)
- `reeves-et-al-2021-encouraging-employee-engagement.pdf` (367 KB)
- `mizrak-et-al-2025-digital-detox.pdf` (939 KB)
