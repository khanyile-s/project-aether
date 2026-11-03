
# Project AETHER — Development Roadmap

## Overview

This roadmap outlines the planned development stages of Project AETHER, from its initial modular structure to a reproducible and automated employment intelligence pipeline.

Development is iterative. Priorities may change as technical challenges are identified and new requirements emerge.

## Phase 1 — Foundation and Architecture

**Status: In progress**

Objectives:
- Establish the GitHub repository
- Define the project scope and objectives
- Create a modular Python architecture
- Develop configurable search terms
- Establish a standardised vacancy data structure
- Implement preliminary relevance filtering
- Develop sponsorship phrase classification
- Initialise an SQLite database
- Implement database storage

## Phase 2 — Documentation and Reproducibility

**Status: In progress**

Objectives:
- Document the project overview
- Describe the pipeline architecture
- Document the search strategy
- Explain the classification methodology
- Provide setup and installation instructions
- Maintain a transparent development roadmap
- Document limitations and assumptions

## Phase 3 — Source Integration

**Status: Planned**

Objectives:
- Identify suitable public vacancy sources
- Investigate official APIs, feeds, and permitted access methods
- Develop source-specific collection modules
- Standardise source-specific vacancy formats
- Introduce error handling and data validation
- Preserve source URLs and collection timestamps

## Phase 4 — Search and Classification Refinement

**Status: Planned**

Objectives:
- Expand job-title synonym dictionaries
- Incorporate skills-based and responsibility-based matching
- Improve relevance filtering
- Refine sponsorship phrase detection
- Investigate negation and contextual language
- Introduce manual validation and labelled test examples
- Evaluate precision, recall, and classification errors

## Phase 5 — Database and Data Quality Improvements

**Status: Planned**

Objectives:
- Expand the database schema as required
- Improve duplicate detection
- Track vacancy updates and changes
- Preserve historical sponsorship evidence
- Introduce data quality checks
- Develop structured queries for analysis

## Phase 6 — Workflow Automation

**Status: Planned**

Objectives:
- Configure GitHub Actions
- Automate scheduled pipeline execution
- Manage configuration and environment variables
- Implement logging and failure reporting
- Prevent duplicate records during repeated runs
- Test workflow execution and reliability

## Phase 7 — Reporting and Analysis

**Status: Planned**

Objectives:
- Generate vacancy summaries
- Analyse vacancies by employer, location, domain, and salary
- Summarise sponsorship evidence
- Identify patterns in job-title terminology
- Export results into CSV or Excel
- Develop visualisations and analytical reports

## Phase 8 — Computational Research Extension

**Status: Future exploration**

Objectives:
- Investigate natural language processing for vacancy classification
- Compare rule-based and machine-learning approaches
- Explore semantic search and text similarity
- Evaluate classification performance using labelled data
- Investigate changes in employment terminology over time

## Long-Term Vision

The long-term objective is to develop a reproducible, modular, and evidence-driven employment intelligence pipeline.

Project AETHER also serves as a practical computational learning project, developing transferable skills in Python programming, data engineering, information retrieval, database management, text analysis, and workflow automation.
