import re

from triviascraper.constants import (
    BLANK,
    EMPTY_STR,
    MATH_FORMAT_RE,
    PARENTHESIS_RE,
)


def get_first_sentence(string):
    """Match only the first sentence of a string."""
    return re.search(r"^((.(?![.?!]+($|\n| [A-Z])))+.)([.?!]+)", string)


def capitalize_first_letter(string):
    """Change only the first character to upper case."""
    return string[0].upper() + string[1:] if string else string


def get_stripped_question(title, sentence, locale_class=None):
    """Remove expected answer from the question, whitespaces and blanks from edges."""
    answer = get_stripped_answer(title)
    # Remove answer from beginning or end of summary.
    question = re.sub(
        f"^({answer}|{title})|({answer}|{title})\.?$",
        EMPTY_STR,
        sentence,
        flags=re.I,
    )
    # Replace remaining occurrences with "blank".
    question = re.sub(f"{answer}|{title}", BLANK, question, flags=re.I)
    # Remove blank with preceding article from beginning of summary.
    if locale_class:
        article_blank_regex = locale_class.get_article_blank_regex()
        question = re.sub(article_blank_regex, EMPTY_STR, question, flags=re.I)
    # Remove formatting
    question = re.sub(r"\n|\t|\r", EMPTY_STR, question)
    question = re.sub(r"\s+", " ", question)
    question = re.sub(MATH_FORMAT_RE, EMPTY_STR, question)
    # Remove parenthesis and ponctuation
    question = re.sub(PARENTHESIS_RE, EMPTY_STR, question).strip(",:.? ")

    return capitalize_first_letter(question)


def get_stripped_answer(title):
    """Remove parenthesis and any content within from answers/titles."""
    return re.sub(PARENTHESIS_RE, EMPTY_STR, title).strip()


def get_stripped_prefix(string, prefix):
    """Remove prefix from string."""
    return re.sub(rf"^{prefix}", EMPTY_STR, string).strip()
