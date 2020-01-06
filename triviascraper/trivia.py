from triviascraper.locale import get_locale_class


class Trivia:
    """Basic definition of a trivia question.

    TODO: use SQLAlchemy.
    """
    question = None  # required
    category = None
    answer = None  # required
    wrong_choices = None
    locale = None

    def __init__(
        self, question="", answer="", locale="", wrong_choices=None, category=""
    ):
        if not answer:
            raise ValueError("Missing answer for trivia")
        if not question:
            raise ValueError("Missing question for trivia")
        self.question = question
        self.category = category
        self.answer = answer
        self.wrong_choices = wrong_choices or []
        if locale_class := get_locale_class(locale):
            try:
                locale = locale_class.get_specific_locale(question, default=locale)
            except Exception as err:
                print(err)
        self.locale = locale

    def __repr__(self):
        return f"<Trivia question=\"{self.question}\" answer=\"{self.answer}\">"

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
