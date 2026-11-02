
from pathlib import Path
import yaml


BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_FILE = BASE_DIR / "config" / "search_terms.yaml"


def load_search_terms():
    """Load keywords from the configuration file."""

    with open(CONFIG_FILE, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def is_relevant_job(job_title):
    """Check whether a job title matches our target keywords."""

    search_terms = load_search_terms()

    all_keywords = [
        keyword.lower()
        for category in search_terms.values()
        for keyword in category
    ]

    title = job_title.lower()

    return any(keyword in title for keyword in all_keywords)


def filter_jobs(jobs):
    """Return only jobs relevant to Project AETHER."""

    relevant_jobs = []

    for job in jobs:
        title = job.get("job_title", "")

        if is_relevant_job(title):
            relevant_jobs.append(job)

    return relevant_jobs


if __name__ == "__main__":
    test_jobs = [
        {"job_title": "Clinical Research Assistant"},
        {"job_title": "Retail Assistant"},
        {"job_title": "Clinical Trial Associate"},
        {"job_title": "Marketing Manager"},
        {"job_title": "Biomedical Scientist"},
    ]

    results = filter_jobs(test_jobs)

    print("Relevant test vacancies:")
    for job in results:
        print(f"- {job['job_title']}")

