
def search_jobs(search_terms):
    """
    Search for job vacancies using keywords.

    Accepts either a list of search terms or a dictionary
    of categories containing lists of search terms.

    Returns:
        list: Collected job vacancies.
    """

    jobs = []

    # If search terms come from YAML as a dictionary,
    # combine all categories into one list.
    if isinstance(search_terms, dict):
        all_terms = [
            term
            for category_terms in search_terms.values()
            for term in category_terms
        ]
    else:
        all_terms = search_terms

    for term in all_terms:
        print(f"Preparing to search for: {term}")

    print(f"\nTotal search terms: {len(all_terms)}")

    return jobs


if __name__ == "__main__":
    example_terms = {
        "clinical_research": [
            "Clinical Research Assistant",
            "Clinical Research Practitioner",
            "Clinical Research Support Worker",
        ]
    }

    results = search_jobs(example_terms)

    print(f"\nTotal vacancies collected: {len(results)}")


