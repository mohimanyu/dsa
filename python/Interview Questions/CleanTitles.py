import re
from collections import Counter


def best_matching_title(clearTitles, rawTitle):
    # Tokenize words from rawTitle (convert to lowercase for case insensitivity)
    raw_words = re.findall(r"\b\w+\b", rawTitle.lower())
    raw_counter = Counter(raw_words)

    max_overlap = 0
    best_title = ""

    for title in clearTitles:
        # Tokenize words from cleanTitle
        title_words = re.findall(r"\b\w+\b", title.lower())
        title_counter = Counter(title_words)

        # Calculate overlap score
        overlap = sum((title_counter & raw_counter).values())

        # Update best title if higher score is found
        if max_overlap < overlap:
            max_overlap = overlap
            best_title = title

    return best_title


clearTitles = ["Software Engineer", "Mechanical Engineer", "Data Scientist"]
rawTitle = "Require a software engineer, paying $10000"

print(best_matching_title(clearTitles, rawTitle))
