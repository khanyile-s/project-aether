
from filter_jobs import filter_jobs
from sponsorship_check import check_sponsorship
from save_jobs import save_jobs
from database import initialise_database


def test_pipeline():
    """Test the core Project AETHER processing pipeline."""

    sample_jobs = [
        {
            "job_title": "Clinical Research Practitioner",
            "employer": "Example NHS Trust",
            "location": "Edinburgh",
            "salary": "£37,000",
            "contract_type": "Fixed-term",
            "closing_date": "2026-12-01",
            "job_url": "https://example.com/job1",
            "source": "Test source",
            "description": (
                "Skilled Worker visa sponsorship is available "
                "for eligible candidates."
            ),
        },
        {
            "job_title": "Retail Assistant",
            "employer": "Example Retailer",
            "location": "Bradford",
            "job_url": "https://example.com/job2",
            "source": "Test source",
            "description": "No sponsorship available.",
        },
    ]

    print("Initialising database...")
    initialise_database()

    print("\nFiltering relevant vacancies...")
    relevant_jobs = filter_jobs(sample_jobs)

    print(f"Relevant vacancies found: {len(relevant_jobs)}")

    print("\nChecking sponsorship wording...")

    for job in relevant_jobs:
        result = check_sponsorship(job.get("description", ""))
        job.update(result)

        print(job["job_title"])
        print(job["sponsorship_status"])

    print("\nSaving vacancies...")
    save_jobs(relevant_jobs)

    print("\nPipeline test completed!")


if __name__ == "__main__":
    test_pipeline()
