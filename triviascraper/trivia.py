from triviascraper.io import DELIMITER, QUOTECHAR


class Trivia:
    """Basic definition of a trivia question.

    TODO: use SQLAlchemy.
    """
    question = None
    category = None
    answer = None
    wrong_choices = None
    locale = None

    def __init__(
        self, question="", answer="", locale="", wrong_choices=None, category=""
    ):
        self.question = question
        self.category = category
        self.answer = answer
        self.wrong_choices = wrong_choices or []
        self.locale = locale

    def strip_answer(self):
        return

    def strip_question(self):
        return

    @property
    def serialized_wrong_choices(self):
        """Serialize list of choices into a string.

        Result is as follows: "choice1,choice2,choice3"
        """
        return ",".join(self.wrong_choices)

    def to_csv(self):
        """Serialize attributes into CSV columns."""
        return (
            self.question,
            self.category,
            self.answer,
            self.serialized_wrong_choices,
            self.locale
        )
