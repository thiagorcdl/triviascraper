import re

PARENTHESIS_RE = r'\([^\)]*\)*'
EMPTY_STR = ""


def get_first_sentence(string):
    """Match only the first sentence of a string."""
    return re.search(r'^((.(?![.?!]+($|\n| [A-Z])))+.)([.?!]+)', string)


def capitalize_first_letter(string):
    """Change only the first character to upper case."""
    return string[0].upper() + string[1:] if string else string


def get_stripped_question(title, new_str, sentence):
    """Remove expected answer from the question, whitespaces and blanks from edges."""
    answer = get_stripped_answer(title)
    # Remove answer from beginning or end of summary.
    question = re.sub(
        f'^({answer}|{title})|({answer}|{title})\.?$',
        EMPTY_STR,
        sentence,
        flags=re.I
    )
    # Replace remaining occurrences with "blank".
    question = re.sub(
        f'{answer}|{title}',
        new_str,
        question,
        flags=re.I
    )
    # Remove parenthesis and ponctuation
    question = re.sub(PARENTHESIS_RE, EMPTY_STR, question).strip(",:.? ")
    return capitalize_first_letter(question)


def get_stripped_answer(title):
    """Remove parenthesis and any content within from answers/titles."""
    return re.sub(PARENTHESIS_RE, EMPTY_STR, title).strip()
