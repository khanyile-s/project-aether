
from database import initialise_database
from process_jobs import process_jobs
from save_jobs import save_jobs


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
            "salary": "£25,000",
            "contract_type": "Permanent",
            "closing_date": "2026-12-15",
            "job_url": "https://example.com/job2",
            "source": "Test source",
            "description": "No sponsorship available.",
        },
    ]

    print("=" * 50)
    print("PROJECT AETHER — PIPELINE TEST")
    print("=" * 50)

    # Step 1: Initialise the database
    print("\n1. Initialising database...")
    initialise_database()

    # Step 2: Process sample vacancies
    print("\n2. Processing sample vacancies...")
    processed_jobs = process_jobs(sample_jobs)

    print(f"Relevant vacancies found: {len(processed_jobs)}")

    # Step 3: Display sponsorship assessments
    print("\n3. Sponsorship assessments:")

    for job in processed_jobs:
        print(f"\nJob: {job['job_title']}")
        print(f"Employer: {job['employer']}")
        print(f"Sponsorship: {job['sponsorship_status']}")
        print(f"Evidence: {job['positive_evidence']}")
        print(f"Negative evidence: {job['negative_evidence']}")

    # Step 4: Save processed vacancies
    print("\n4. Saving vacancies...")
    saved_count = save_jobs(processed_jobs)

    # Step 5: Report results
    print("\n" + "=" * 50)
    print("PIPELINE TEST RESULTS")
    print("=" * 50)
    print(f"Sample vacancies: {len(sample_jobs)}")
    print(f"Relevant vacancies: {len(processed_jobs)}")
    print(f"New records saved: {saved_count}")
    print("\nPipeline test completed!")


if __name__ == "__main__":
    test_pipeline()

