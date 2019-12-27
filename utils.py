import re

PARENTHESIS_RE = r'(\(.+\))'
EMPTY_STR = ""


def get_first_sentence(string):
    """Match only the first sentence of a string."""
    return re.search(r'^((.(?![.?!:]+($|\n| [A-Z])))+.)([.?!:]+)', string)


def get_stripped_question(title, new_str, sentence):
    """Remove expected answer from the question, whitespaces and blanks from edges."""
    answer = get_stripped_answer(title)
    question = re.sub(
        f'({answer}|{title})',
        new_str,
        sentence,
        flags=re.I
    )
    question = re.sub(PARENTHESIS_RE, EMPTY_STR, question)
    return question.strip().strip(new_str).strip()


def get_stripped_answer(title):
    """Remove parenthesis and any content inside from answers/titles."""
    return re.sub(PARENTHESIS_RE, EMPTY_STR, title).strip()
