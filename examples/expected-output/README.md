# Expected Output Examples

This directory contains example outputs from a successful execution of the research workflow.

## Files

### `parsed_papers.json`
Structured data extracted from the three research papers, including:
- Paper metadata (authors, year, title, venue)
- Study details (participants, methods, instruments)
- Statistical results (correlations, regression, SEM)
- Key findings and recommendations

### `correlation_analysis.json`
Statistical analysis synthesizing findings across all papers:
- Experience-fatigue relationship
- Key correlations (fatigue↔productivity, fatigue↔mental health)
- Regression and SEM results
- Sector-specific analysis
- Intervention effectiveness

### `draft_article.md`
Publication-ready article (1,247 words) about cybersecurity fatigue research:
- Professional tone for technology/business audiences
- Full statistical reporting (r, n, p-value)
- Proper citations for all three papers
- Practical implications for organizations

### `review_feedback.json`
Quality control review showing "APPROVED" status after revision cycle:
- Initial review identified 5 issues (1 critical, 2 major, 2 minor)
- All issues addressed through revision
- Final approval granted

## Using These Examples

When running the tutorial:
1. Your `results/` directory should initially be empty
2. After running the orchestrator workflow, your outputs should match these examples
3. Compare your generated files against these to verify correct execution
