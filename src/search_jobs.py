
from datetime import date


def create_job_record(
    job_title,
    employer,
    job_url,
    source,
    location="Unknown",
    salary="Not specified",
    contract_type="Not specified",
    closing_date=None,
    description="",
):
    """
    Create a standardised vacancy record for Project AETHER.
    """

    return {
        "job_title": job_title,
        "employer": employer,
        "location": location,
        "salary": salary,
        "contract_type": contract_type,
        "closing_date": closing_date,
        "job_url": job_url,
        "source": source,
        "description": description,
        "date_discovered": date.today().isoformat(),
        "last_checked": date.today().isoformat(),
        "sponsorship_status": "Unverified",
        "sponsor_register_status": "Unknown",
        "eligibility_status": "Not assessed",
        "notes": "",
    }


def search_jobs(search_terms):
    """
    Search for vacancies using keywords.

    Currently prepares the search terms.
    Live vacancy collection will be added next.
    """

    jobs = []

    if isinstance(search_terms, dict):
        all_terms = [
            term
            for category_terms in search_terms.values()
            for term in category_terms
        ]
    else:
        all_terms = search_terms

    for term in all_terms:
        print(f"Search term prepared: {term}")

    print(f"\nTotal search terms: {len(all_terms)}")

    return jobs


if __name__ == "__main__":
    example = create_job_record(
        job_title="Clinical Research Practitioner",
        employer="Example NHS Trust",
        job_url="https://example.com/job",
        source="Example source",
        location="Edinburgh",
    )

    print("Example vacancy record:")
    print(example)



