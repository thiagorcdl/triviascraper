import re

from triviascraper.constants import EMPTY_STR
from triviascraper.locale import get_locale_class


class Trivia:
    """Basic definition of a trivia question.

    TODO: use SQLAlchemy.
    """

    question = None  # required
    answer = None  # required
    wrong_choices = None
    locale = None
    category = None

    def __init__(
        self,
        question="",
        answer="",
        locale="",
        wrong_choices=None,
        categories=None,
    ):
        if not answer:
            raise ValueError("Missing answer for trivia")
        if not question:
            raise ValueError("Missing question for trivia")
        self.question = question
        self.answer = answer
        self.wrong_choices = wrong_choices or []

        if locale_class := get_locale_class(locale):
            self.category = self.get_mapped_category(categories, locale_class)
            locale = locale_class.get_specific_locale(question, default=locale)

        self.locale = locale

    def __repr__(self):
        return f'<Trivia question="{self.question}" answer="{self.answer}">'

    def get_mapped_category(self, categories, locale_class):
        """Normalize category based on options."""
        for category in categories or []:
            for mapped, terms in locale_class.category_mapping.items():
                if any(
                    [re.search(term, category, flags=re.I) for term in terms]
                ):
                    return mapped
        return EMPTY_STR

    def serialize_list(self, items):
        """Serialize list into a comma-separated string.

        Result is as follows: "item1,item2,item3"
        """
        return ",".join(items)

    @property
    def serialized_wrong_choices(self):
        """Serialize list of choices into a string."""
        return self.serialize_list(self.wrong_choices)

    def to_csv(self):
        """Serialize attributes into CSV columns."""
        return (
            self.question,
            self.category,
            self.answer,
            self.serialized_wrong_choices,
            self.locale,
        )
