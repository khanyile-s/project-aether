
# Project AETHER — Methodology

## 1. Overview

Project AETHER uses a structured, evidence-based methodology to discover, process, and assess UK employment vacancies relevant to international candidates.

The methodology combines information retrieval, data standardisation, rule-based text analysis, and structured data storage.

## 2. Vacancy Discovery

Vacancies are identified using configurable search terms across professional domains.

Search criteria incorporate:
- Job titles and title variations
- Technical skills
- Professional responsibilities
- Research domains
- Relevant employment terminology

The project aims to use publicly accessible and appropriately authorised data sources.

## 3. Data Standardisation

Collected vacancy information is converted into a standardised record.

This process allows data from different recruitment sources to be stored and analysed consistently.

Standardisation includes:
- Normalising field names
- Handling missing information
- Recording source URLs
- Capturing discovery dates
- Maintaining consistent data types where possible

Missing information is retained as unknown or unspecified rather than inferred.

## 4. Relevance Classification

Vacancies are initially evaluated using rule-based keyword matching.

The system compares vacancy titles against configurable search terms to determine whether they are potentially relevant.

This approach is transparent and computationally inexpensive, but it has limitations.

For example:
- Relevant vacancies may use unexpected terminology.
- Keywords may appear in unrelated roles.
- Job titles may not adequately describe responsibilities.

Future iterations may incorporate skills-based matching and semantic similarity.

## 5. Sponsorship Evidence Classification

Vacancy descriptions are examined for predefined phrases associated with visa sponsorship.

### Classification Categories

| Category | Interpretation |
|---|---|
| Explicit positive wording | Text indicates sponsorship may be available |
| Explicit negative wording | Text indicates sponsorship is unavailable |
| Conflicting evidence | Both positive and negative indicators are detected |
| Unclear | No decisive sponsorship wording is detected |

### Rule-Based Approach

The preliminary classifier uses phrase matching.

When a phrase is detected, it is recorded as evidence supporting the corresponding classification.

The purpose is to identify vacancies requiring further investigation, not to make final decisions about immigration eligibility.

## 6. Evidence and Uncertainty

The absence of sponsorship wording does not establish that an employer cannot sponsor a candidate.

Similarly, an employer's inclusion on the UK Register of Licensed Sponsors does not establish that a specific vacancy is eligible for sponsorship.

AETHER therefore treats the following as separate questions:

1. Is the employer licensed to sponsor workers?
2. Does the vacancy explicitly mention sponsorship?
3. Is the role potentially eligible under the applicable occupation requirements?
4. Are the salary, qualification, and other requirements satisfied?
5. Has the employer confirmed sponsorship for this particular position?

These questions require distinct evidence sources and, where appropriate, manual verification.

## 7. Data Storage and Deduplication

Vacancy records are stored in an SQLite database.

The job URL serves as the primary identifier for detecting duplicate listings where a valid URL is available.

Database constraints help prevent repeated insertion of the same vacancy.

Further improvements may include:
- URL normalisation
- Duplicate detection when URLs differ
- Tracking updated vacancy descriptions
- Recording historical changes in sponsorship wording

## 8. Evaluation

The system's performance should be evaluated using manually reviewed examples.

Potential evaluation metrics include:

### Precision

The proportion of vacancies classified as relevant that are genuinely relevant.

### Recall

The proportion of genuinely relevant vacancies successfully identified.

### Classification Accuracy

The proportion of sponsorship assessments that agree with manually reviewed evidence.

### Error Analysis

False positives and false negatives should be examined to identify weaknesses in the search and classification rules.

## 9. Limitations

The methodology has several limitations:

- Keyword matching may miss relevant vacancies.
- Phrase-based sponsorship classification may misinterpret context.
- Job advertisements may omit important information.
- Vacancy details may change after collection.
- Automated text analysis cannot determine full immigration eligibility.
- Different recruitment sources may have inconsistent formats.

These limitations make manual verification an essential part of the process.

## 10. Ethical Considerations

AETHER is intended to support informed decision-making rather than replace human judgement.

The project will:
- Preserve source information for verification
- Distinguish evidence from inference
- Represent uncertainty transparently
- Avoid unsupported claims about sponsorship
- Respect source access restrictions
- Document methodological limitations

## 11. Future Research Directions

Future development may investigate:
- Natural language processing
- Semantic similarity for vacancy matching
- Improved negation and context detection
- Classification evaluation using labelled data
- Monitoring changes in sponsorship language
- Comparative performance of rule-based and machine-learning approaches
