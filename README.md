# SAPHO Gene Analysis Pipeline

> AI-driven gene analysis pipeline for SAPHO syndrome research
> Input a gene name -> auto-query ClinVar/PubMed -> generate structured report

## What is this?

SAPHO (Synovitis-Acne-Pustulosis-Hyperostosis-Osteitis) is a rare autoimmune syndrome. This project provides an **AI-powered gene analysis workflow** that:

- Queries known SAPHO-associated genes from a curated knowledge base
- Fetches variant data from **ClinVar** (NCBI public database)
- Searches latest literature from **PubMed**
- Generates structured Markdown analysis reports
- Supports single-gene and multi-gene batch analysis

## Quick Start

\\ash
pip install requests

# List known SAPHO genes
python scripts/sapho_analysis_pipeline.py --list

# Analyze a single gene
python scripts/sapho_analysis_pipeline.py IL36RN

# Batch analyze all genes
python scripts/sapho_analysis_pipeline.py --all
\
## Core Genes

| Gene | Locus | Evidence | Mechanism |
|------|-------|----------|-----------|
| IL36RN | 2q14.1 | High | IL-1 pathway overactivation |
| PSTPIP1 | 15q24.3 | Strong | PAPA/SAPHO spectrum |
| LPIN2 | 18p11.31 | Strong | Majeed/SAPHO overlap |
| NOD2 | 16q12.1 | Moderate | NOD signaling |
| IL1RN | 2q14.1 | Moderate | IL-1 receptor antagonist |

## Output

Each analysis generates a Markdown report containing:
- Gene info (name, locus, OMIM ID)
- Pathomechanism
- Known variants with dbSNP IDs
- ClinVar search results
- PubMed literature count
- Therapeutic implications

## Reusable Template

The \	emplate_workflow.py\ is a disease-agnostic template. Replace 4 placeholders to adapt it to any gene-disease analysis.

## License

MIT
