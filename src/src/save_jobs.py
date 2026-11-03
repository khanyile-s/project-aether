
from database import get_connection


def save_jobs(jobs):
    """Save collected job vacancies to the database."""

    connection = get_connection()
    saved_count = 0

    for job in jobs:
        try:
            connection.execute("""
                INSERT OR IGNORE INTO vacancies (
                    job_title,
                    employer,
                    location,
                    salary,
                    contract_type,
                    closing_date,
                    job_url,
                    source,
                    sponsorship_status,
                    date_discovered,
                    last_checked,
                    notes
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                job.get("job_title"),
                job.get("employer"),
                job.get("location"),
                job.get("salary"),
                job.get("contract_type"),
                job.get("closing_date"),
                job.get("job_url"),
                job.get("source"),
                job.get("sponsorship_status", "Unverified"),
                job.get("date_discovered"),
                job.get("last_checked"),
                job.get("notes")
            ))

            saved_count += connection.execute(
                "SELECT changes()"
            ).fetchone()[0]

        except Exception as error:
            print(f"Could not save vacancy: {error}")

    connection.commit()
    connection.close()

    print(f"New vacancies saved: {saved_count}")

    return saved_count
