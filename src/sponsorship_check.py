
POSITIVE_PHRASES = [
    "visa sponsorship available",
    "visa sponsorship is available",
    "sponsorship is available",
    "we offer visa sponsorship",
    "skilled worker sponsorship",
    "certificate of sponsorship",
    "we can sponsor",
]

NEGATIVE_PHRASES = [
    "unable to offer sponsorship",
    "cannot offer sponsorship",
    "no visa sponsorship",
    "no sponsorship available",
    "unable to sponsor",
    "must have the right to work in the uk",
    "no certificate of sponsorship",
]


def check_sponsorship(job_description):
    """
    Classify sponsorship wording in a job description.

    This is a preliminary text check, not a legal
    determination of visa eligibility.
    """

    text = job_description.lower()

    positive_matches = [
        phrase for phrase in POSITIVE_PHRASES
        if phrase in text
    ]

    negative_matches = [
        phrase for phrase in NEGATIVE_PHRASES
        if phrase in text
    ]

    if positive_matches and negative_matches:
        status = "Conflicting evidence"

    elif positive_matches:
        status = "Explicit positive wording"

    elif negative_matches:
        status = "Explicit negative wording"

    else:
        status = "Unclear - manual verification"

    return {
        "sponsorship_status": status,
        "positive_evidence": positive_matches,
        "negative_evidence": negative_matches,
    }


if __name__ == "__main__":

    example = """
    We welcome international applicants.
    Skilled Worker visa sponsorship is available
    for eligible candidates.
    """

    result = check_sponsorship(example)

    print("Sponsorship assessment:")
    print(result)

