
# Project AETHER — Pipeline Architecture

## 1. Overview

Project AETHER is designed as a modular data pipeline.

A modular architecture separates the system into components with distinct responsibilities. Each component can be developed, tested, and maintained independently.

The planned pipeline follows these stages:

1. Search
2. Standardisation
3. Relevance filtering
4. Sponsorship assessment
5. Database storage
6. Reporting

## 2. System Architecture

```text
           Search Configuration
             (search_terms.yaml)
                    |
                    v
             Search Module
            (search_jobs.py)
                    |
                    v
         Vacancy Standardisation
            (create_job_record)
                    |
                    v
           Relevance Filtering
            (filter_jobs.py)
                    |
                    v
       Sponsorship Text Assessment
          (sponsorship_check.py)
                    |
                    v
            Processing Module
           (process_jobs.py)
                    |
                    v
            Database Storage
             (save_jobs.py)
                    |
                    v
             SQLite Database
             (database.py)
                    |
                    v
          Reporting and Analysis
             (Planned)
```

## 3. Component Responsibilities

### Search Configuration

File: `config/search_terms.yaml`

Stores configurable search terms organised by professional domain.

Separating configuration from application logic allows search criteria to be updated without rewriting the Python code.

### Search Module

File: `src/search_jobs.py`

Responsible for preparing search queries and, in future development, collecting vacancy information from approved public sources.

The module also standardises collected information into a consistent vacancy record.

### Relevance Filtering

File: `src/filter_jobs.py`

Evaluates whether a vacancy is relevant to the project's defined employment domains.

The initial approach uses keyword matching. Future iterations may incorporate skills, responsibilities, and semantic similarity.

### Sponsorship Assessment

File: `src/sponsorship_check.py`

Examines vacancy descriptions for explicit sponsorship-related wording.

The module identifies positive, negative, conflicting, or unclear evidence.

This is a preliminary text classification process rather than an immigration eligibility assessment.

### Processing Module

File: `src/process_jobs.py`

Coordinates the processing stages by passing collected vacancies through relevance filtering and sponsorship assessment.

This separation makes the pipeline easier to test and extend.

### Database Module

File: `src/database.py`

Initialises and manages the SQLite database connection and schema.

The database is designed to preserve vacancy information for subsequent querying, comparison, and analysis.

### Storage Module

File: `src/save_jobs.py`

Writes processed vacancy records into the database.

Duplicate vacancy URLs are handled using database-level uniqueness constraints.

## 4. Data Flow

Each vacancy is represented as a structured record containing fields such as:

- Job title
- Employer
- Location
- Salary
- Contract type
- Closing date
- Job URL
- Source
- Description
- Sponsorship assessment
- Discovery and verification dates

Standardising these fields allows information from different sources to be analysed consistently.

## 5. Design Principles

### Modularity

Each component performs a clearly defined task.

### Reusability

Functions can be reused across different data sources and workflows.

### Configurability

Search terms and criteria are stored separately from the core code.

### Reproducibility

Version control and structured configuration support consistent execution and tracking of changes.

### Extensibility

Additional sources, classification approaches, and reporting functionality can be incorporated without redesigning the entire system.

## 6. Current Limitations

The architecture is still evolving.

The search module currently prepares search terms rather than retrieving live vacancies. Source integrations, automated scheduling, and reporting have not yet been implemented.

The architecture diagram represents the intended pipeline, not a claim that all stages are currently operational.

## 7. Future Development

Planned improvements include:

- Integrating authorised vacancy sources
- Expanding relevance classification beyond job titles
- Improving sponsorship evidence extraction
- Adding data validation and error handling
- Implementing automated execution through GitHub Actions
- Developing analytical reports and vacancy summaries
