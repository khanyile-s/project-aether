
# Project AETHER — Project Overview

## 1. Introduction

Project AETHER (Automated Employment & Talent Horizon Exploration and Research) is a Python-based research and data pipeline designed to identify, collect, standardise, and analyse UK employment opportunities relevant to international candidates seeking Skilled Worker visa sponsorship.

The project focuses on roles aligned with clinical research, clinical trial operations, research governance, biomedical science, quality assurance, and regulatory affairs.

## 2. Motivation

Finding suitable employment opportunities as an international graduate can be challenging because:

- Relevant vacancies are distributed across multiple recruitment platforms.
- Job titles vary significantly between employers.
- Sponsorship information is often inconsistent or absent.
- An employer's sponsorship licence does not guarantee that every vacancy is eligible for sponsorship.
- Manual searching is time-consuming and difficult to reproduce systematically.

AETHER aims to make this process more structured, transparent, and evidence-driven.

## 3. Project Objectives

The primary objectives are to:

1. Identify relevant UK employment opportunities from publicly accessible sources.
2. Standardise vacancy information into a consistent data structure.
3. Filter opportunities according to professional relevance.
4. Examine vacancy descriptions for sponsorship-related evidence.
5. Store collected information in a structured database.
6. Support reproducible searches and systematic monitoring.
7. Generate reports that support informed career decisions.

## 4. Research Domains

The project investigates employment opportunities across the following domains:

### Clinical Research and Trial Operations
- Clinical Research Support Worker
- Clinical Research Practitioner
- Clinical Trial Assistant
- Clinical Trial Associate
- Study Coordinator
- Research Delivery roles

### Research Governance and Management
- Research Governance Officer
- Research Management
- Research Facilitator
- Clinical Research Coordinator

### Quality and Regulatory Affairs
- GCP Quality Assurance
- Clinical Quality
- Regulatory Affairs
- Trial Master File (TMF) management
- Clinical documentation

### Biomedical and Translational Science
- Biomedical Scientist
- Clinical Scientist
- Specialist laboratory roles
- Translational and cancer research positions

Job discovery will use a combination of title-based, skill-based, and responsibility-based search strategies.

## 5. Technical Approach

AETHER is being developed using a modular Python architecture.

| Component | Purpose |
|---|---|
| Python | Core programming language |
| YAML | Configurable search terms |
| Requests | HTTP requests |
| BeautifulSoup | HTML parsing |
| SQLite | Structured vacancy storage |
| Pandas | Data analysis |
| GitHub | Version control |
| GitHub Actions | Planned workflow automation |

## 6. Sponsorship Assessment

Vacancy descriptions will be examined for sponsorship-related language.

Evidence will be classified into four preliminary categories:

- Explicit positive wording
- Explicit negative wording
- Conflicting evidence
- Unclear — manual verification required

These classifications represent textual evidence, not legal determinations.

Employer sponsorship status, individual vacancy sponsorship, occupation eligibility, salary requirements, and other immigration conditions must be evaluated separately.

## 7. Development Status

Project AETHER is currently in early development.

Implemented components include:
- Search-term configuration
- Vacancy record standardisation
- Relevance filtering
- Preliminary sponsorship-text assessment
- Database initialisation
- Database storage functionality

Live vacancy collection, source-specific integrations, automated execution, and reporting remain under development.

## 8. Ethical and Methodological Considerations

The project will prioritise publicly accessible and appropriately authorised data sources.

It will not rely on unauthorised access, circumvent platform restrictions, or assume that missing information constitutes negative evidence.

All automated classifications should remain transparent, reproducible, and subject to human verification.

## 9. Long-Term Vision

The long-term goal is to develop a reproducible employment intelligence pipeline that combines information retrieval, data engineering, rule-based text analysis, and workflow automation.

The project also provides an opportunity to develop transferable computational skills relevant to biomedical data science, research informatics, and interdisciplinary research.
