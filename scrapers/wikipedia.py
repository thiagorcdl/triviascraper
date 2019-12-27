import re

from scrapers.base import BaseScraper
import wikipedia

from utils import get_first_sentence, get_stripped_answer, get_stripped_question


class WikipediaScraper(BaseScraper):
    titles = []

    def __init__(self, n_questions, lang):
        super(WikipediaScraper, self).__init__(n_questions, lang)
        wikipedia.set_lang(lang)
        self.titles = self.get_random_titles()

    def get_random_titles(self):
        """Return a list of random Wikipedia titles."""
        return wikipedia.random(pages=self.n_questions)

    def get_random_title(self):
        """Return next random Wikipedia title."""
        for title in self.titles:
            yield title

    def fetch_article(self, *args, **kwargs):
        """Fetch a single article from the base URL."""
        try:
            article = wikipedia.page(*args, auto_suggest=False, **kwargs)
        except wikipedia.DisambiguationError:
            article = None
        return article

    @property
    def iterator(self, *args, **kwargs):
        """Iterate through random titles."""
        return self.get_random_title()

    def parse_article(self, article):
        """Get first sentence of the summary and remvoe answer from it."""
        if first_sentence := get_first_sentence(article.summary):
            question = get_stripped_question(
                article.title, self.BLANK, first_sentence.group()
            )
            return {
                'answer': get_stripped_answer(article.title),
                'question': question,
                'locale': self.lang,
            }

    def write_question(self, question_data):
        """Parse through article text and extract question components."""
        print(question_data)  # TODO: remove override
