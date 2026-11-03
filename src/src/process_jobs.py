
from filter_jobs import filter_jobs
from sponsorship_check import check_sponsorship


def process_jobs(jobs):
    """
    Filter vacancies and assess their sponsorship wording.

    Returns a list of relevant vacancies with assessments.
    """

    relevant_jobs = filter_jobs(jobs)

    for job in relevant_jobs:
        description = job.get("description", "")

        assessment = check_sponsorship(description)

        job.update(assessment)

    return relevant_jobs


if __name__ == "__main__":
    sample_jobs = [
        {
            "job_title": "Clinical Research Practitioner",
            "employer": "Example NHS Trust",
            "description": (
                "We offer Skilled Worker visa sponsorship "
                "for eligible candidates."
            ),
        },
        {
            "job_title": "Retail Assistant",
            "employer": "Example Retailer",
            "description": "No sponsorship available.",
        },
    ]

    results = process_jobs(sample_jobs)

    print("\nProcessed vacancies:")

    for job in results:
        print(job["job_title"])
        print(job["sponsorship_status"])
