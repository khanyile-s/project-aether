
# Project AETHER — Search Strategy

## 1. Purpose

The search strategy defines how Project AETHER identifies potentially relevant employment opportunities across the United Kingdom.

The objective is to maximise relevant vacancy discovery while minimising irrelevant results and missed opportunities.

## 2. The Challenge of Job Title Variability

Employers frequently use different titles for similar responsibilities.

For example, clinical research delivery roles may be advertised as:

- Clinical Research Support Worker
- Clinical Research Practitioner
- Research Delivery Officer
- Research Nurse Support
- Research Assistant
- Clinical Trial Coordinator

A search strategy restricted to a small number of exact job titles may fail to identify relevant opportunities.

AETHER therefore uses a broader, multi-dimensional approach.

## 3. Search Dimensions

### A. Job Title-Based Search

Searches use variations of relevant professional titles.

Examples:
- Clinical Research Assistant
- Clinical Trial Assistant
- Clinical Research Practitioner
- Research Delivery
- Study Coordinator
- Research Governance Officer
- Clinical Quality Associate

### B. Skills-Based Search

Searches incorporate transferable skills and technical competencies.

Examples:
- Good Clinical Practice (GCP)
- Clinical trial documentation
- Trial Master File (TMF)
- Data management
- Regulatory compliance
- Participant recruitment
- Research coordination

### C. Responsibility-Based Search

Searches consider the duties described in vacancy advertisements.

Examples:
- Supporting clinical trial delivery
- Coordinating research activities
- Maintaining study documentation
- Supporting research governance
- Collecting and managing research data
- Assisting with participant visits

## 4. Boolean Search Logic

Boolean operators help combine and refine search terms.

| Operator | Function | Example |
|---|---|---|
| AND | Requires both concepts | Clinical Research AND Coordinator |
| OR | Accepts alternatives | Research Assistant OR Research Practitioner |
| NOT | Excludes a concept | Research Assistant NOT PhD |

Parentheses group related concepts together.

Example:

```text
("Clinical Research" OR "Research Delivery"
OR "Clinical Trial")
AND
("Assistant" OR "Practitioner"
OR "Coordinator" OR "Support Worker")
```

Search syntax varies between platforms, so queries may need to be adapted to each source.

## 5. Domain-Based Search Categories

AETHER currently organises searches around four major domains:

1. Clinical research and trial operations
2. Research governance and management
3. Quality assurance and regulatory affairs
4. Biomedical and translational science

These categories will evolve as new relevant vacancies and terminology are identified.

## 6. NHS-Specific Search Considerations

NHS vacancies may use terminology that differs from private-sector recruitment.

Searches should account for:

- Agenda for Change bands
- Research delivery teams
- Clinical research networks
- NHS Trust-specific terminology
- Research support and coordination titles
- Fixed-term and substantive contracts

AETHER should not exclude a potentially relevant vacancy solely because its title differs from the initial keyword list.

## 7. Sponsorship-Aware Discovery

Job relevance and sponsorship evidence are separate analytical dimensions.

A vacancy may be professionally relevant but explicitly unavailable for sponsorship.

Conversely, a vacancy may mention sponsorship but fall outside the project's target professional domains.

The search strategy therefore aims to identify relevant vacancies first, then assess sponsorship evidence independently.

## 8. Search Evaluation

The effectiveness of the search strategy can be assessed using:

### Precision

The proportion of retrieved vacancies that are genuinely relevant.

### Recall

The proportion of relevant vacancies successfully identified by the search system.

### False Positives

Retrieved vacancies that do not meet the project's relevance criteria.

### False Negatives

Relevant vacancies missed by the search system.

These concepts will help guide improvements to search terms and classification rules.

## 9. Future Improvements

Planned improvements include:

- Expanding title synonym dictionaries
- Incorporating skills and responsibility-based matching
- Evaluating search results against manually reviewed vacancies
- Comparing search strategies across recruitment platforms
- Exploring semantic search and natural language processing
- Tracking changes in vacancy terminology over time
