# Project AETHER
### Automated Employment & Talent Horizon Exploration and Research

## Overview

Project AETHER is a Python-based job discovery and intelligence
pipeline designed to identify UK employment opportunities
potentially eligible for Skilled Worker visa sponsorship.

The project focuses on clinical research, clinical trial
operations, research governance, biomedical science,
quality assurance, and adjacent scientific career pathways.

## Motivation

Conventional job searches rely heavily on exact job titles
and manual screening.

AETHER explores a more systematic approach by combining
keyword-based retrieval, Boolean search strategies,
skills-based matching, vacancy filtering, and sponsorship
evidence classification.

The long-term objective is to reduce manual search effort
while improving the identification of relevant opportunities.

## Research Questions

- Can structured search strategies improve vacancy discovery?
- Can transferable skills identify relevant roles beyond
  conventional job-title searches?
- How reliably can sponsorship wording be classified
  automatically?
- How can vacancy information be organised for systematic
  comparison and longitudinal monitoring?

## Target Career Domains

- Clinical research and clinical trial operations
- Research delivery and research coordination
- Research governance and management
- GCP quality assurance and regulatory affairs
- Trial documentation and data management
- Biomedical science and translational research
- Related biomedical and healthcare research positions

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming and processing |
| YAML | Search configuration |
| SQLite | Structured vacancy storage |
| pandas | Data manipulation and analysis |
| requests | HTTP communication |
| BeautifulSoup | HTML parsing |
| Git | Version control |
| GitHub | Repository hosting and collaboration |
| GitHub Actions | Planned workflow automation |

## Pipeline Architecture

The planned pipeline consists of:

1. Search configuration
2. Vacancy retrieval
3. Vacancy standardisation
4. Relevance filtering
5. Sponsorship evidence classification
6. Database storage
7. Reporting and analysis
8. Scheduled automation

## Sponsorship Assessment

AETHER distinguishes between:

- Explicit positive sponsorship wording
- Explicit negative sponsorship wording
- Conflicting evidence
- Unclear or unverified information

Employer presence on the UK sponsor register alone does not
establish that a particular vacancy offers sponsorship.

Automated classifications are preliminary and require
verification against official sources and applicable
immigration requirements.

## Current Development Status

**Status: Early development**

The foundational modules and initial database structure
have been created.

Live vacancy collection, complete pipeline integration,
automated validation, reporting, and scheduled execution
remain under development.

## Future Development

- Expand Boolean and skills-based search strategies
- Integrate accessible public vacancy sources
- Improve vacancy deduplication and historical tracking
- Introduce relevance scoring
- Evaluate natural language processing approaches
- Explore machine learning for semantic job matching
- Implement scheduled GitHub Actions workflows
- Develop analytical dashboards and reports

## Disclaimer

Project AETHER is an independent research and career
intelligence project. It does not provide immigration
advice or guarantee sponsorship or employment eligibility.
All vacancy and sponsorship information requires
independent verification.
