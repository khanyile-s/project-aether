
from pathlib import Path
import yaml

from database import initialise_database
from process_jobs import process_jobs
from save_jobs import save_jobs


BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_FILE = BASE_DIR / "config" / "search_terms.yaml"


def load_search_terms():
    """Load job search keywords from YAML."""
    with open(CONFIG_FILE, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def main():
    print("=" * 50)
    print("PROJECT AETHER")
    print("UK Sponsorship Job Intelligence Pipeline")
    print("=" * 50)

    initialise_database()

    search_terms = load_search_terms()

    print(f"\nSearch categories loaded: {len(search_terms)}")

    print("\nDatabase initialised.")
    print("Pipeline ready to process vacancies!")


if __name__ == "__main__":
    main()

