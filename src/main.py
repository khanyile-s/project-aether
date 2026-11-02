
from pathlib import Path
import yaml


# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Search terms configuration
CONFIG_FILE = BASE_DIR / "config" / "search_terms.yaml"


def load_search_terms():
    """Load job search keywords from the YAML configuration."""
    with open(CONFIG_FILE, "r", encoding="utf-8") as file:
        search_terms = yaml.safe_load(file)

    return search_terms


def main():
    search_terms = load_search_terms()

    print("PROJECT AETHER")
    print("=" * 40)
    print("Search categories loaded successfully!\n")

    for category, terms in search_terms.items():
        print(f"\n{category.upper()}")

        for term in terms:
            print(f" - {term}")

    print("\nConfiguration loaded. Ready for the next stage!")


if __name__ == "__main__":
    main()

