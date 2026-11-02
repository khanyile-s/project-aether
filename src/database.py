
import sqlite3
from pathlib import Path


# Project directories
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

# Database location
DB_PATH = DATA_DIR / "aether.db"


def get_connection():
    """Connect to the Project AETHER database."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row

    return connection


def initialise_database():
    """Create the vacancies table if it does not exist."""

    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS vacancies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            job_title TEXT NOT NULL,
            employer TEXT NOT NULL,
            location TEXT,

            salary TEXT,
            contract_type TEXT,
            closing_date TEXT,

            job_url TEXT UNIQUE,
            source TEXT,

            sponsorship_status TEXT DEFAULT 'Unverified',
            sponsor_register_status TEXT DEFAULT 'Unknown',
            eligibility_status TEXT DEFAULT 'Not assessed',

            date_discovered TEXT,
            last_checked TEXT,

            notes TEXT
        )
    """)

    connection.commit()
    connection.close()

    print("Project AETHER database initialised successfully!")


if __name__ == "__main__":
    initialise_database()

