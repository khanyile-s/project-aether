
# Project AETHER — Setup Guide

## 1. Overview

This guide explains how to set up Project AETHER in a local Python environment.

The project is currently under active development. Live vacancy collection and automated execution are not yet implemented.

## 2. Prerequisites

The following software is required:

- Python 3.10 or later
- Git
- A code editor (Visual Studio Code is recommended)
- A GitHub account

## 3. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/YOUR-USERNAME/project-aether.git
```

Navigate into the project directory:

```bash
cd project-aether
```

Replace `YOUR-USERNAME` with your GitHub username.

## 4. Create a Virtual Environment

A virtual environment isolates the project's dependencies from other Python projects.

Create the environment:

```bash
python -m venv .venv
```

Activate it.

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

## 5. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

The dependencies currently include:

- PyYAML
- Pandas
- Requests
- BeautifulSoup
- OpenPyXL

## 6. Run the Project

From the project root directory, execute:

```bash
python src/main.py
```

The current application is in early development. Depending on the latest implementation, this command may initialise or demonstrate the pipeline components without retrieving live vacancies.

## 7. Initialise the Database

To initialise the SQLite database, run:

```bash
python src/database.py
```

The database file is created inside the `data/` directory.

SQLite is included with Python, so no separate database server is required.

## 8. Project Structure

```text
project-aether/
│
├── .github/
│   └── workflows/
│
├── config/
│   └── search_terms.yaml
│
├── data/
│   └── .gitkeep
│
├── docs/
│
├── reports/
│   └── .gitkeep
│
├── src/
│   ├── database.py
│   ├── filter_jobs.py
│   ├── main.py
│   ├── process_jobs.py
│   ├── save_jobs.py
│   ├── search_jobs.py
│   └── sponsorship_check.py
│
├── requirements.txt
└── README.md
```

## 9. Configuration

Search terms are maintained in:

`config/search_terms.yaml`

This file can be edited to expand or refine the search vocabulary without changing the core Python modules.

## 10. Troubleshooting

### ModuleNotFoundError

Ensure that:
- The virtual environment is activated.
- Dependencies have been installed.
- Commands are being executed from the project root.

### FileNotFoundError

Check that:
- The repository directory structure is correct.
- The configuration file exists.
- Commands are executed from the expected location.

### Database Issues

Ensure that:
- The `data/` directory exists or can be created.
- The project has permission to write to the directory.

## 11. Development Notes

Project AETHER is being developed incrementally.

Future setup instructions will include:
- Source-specific configuration
- API credentials, if required
- GitHub Actions workflow configuration
- Automated execution and reporting
