import requests


class BaseScraper:
    BLANK = '____'
    URL = ""
    n_questions = 0
    lang = "en"

    def __init__(self, n_questions, lang):
        self.n_questions = n_questions
        self.lang = lang

    def fetch_article(self, *args, **kwargs):
        """Fetch a single article from the base URL."""
        return requests.get(self.URL, *args, **kwargs)

    @property
    def iterator(self, *args, **kwargs):
        """Define iteration base for fetching the articles."""
        return range(self.n_questions)

    def fetch_articles(self):
        """Yield list of articles."""
        for i in self.iterator:
            yield self.fetch_article(i)

    def parse_article(self, article):
        """Parse through article text and extract question components."""
        raise NotImplementedError

    def write_question(self, question_data):
        """Parse through article text and extract question components."""
        raise NotImplementedError  # TODO: implement this

    def get_questions(self, write=False):
        """Get n articles and turn them into questions."""
        for article in self.fetch_articles():
            if not article:
                continue
            question_data = self.parse_article(article)
            if write:
                self.write_question(question_data)

    def run(self):
        """Run main logic (get and write questions)."""
        self.get_questions(write=True)
