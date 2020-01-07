from triviascraper.locale import get_locale_class
from triviascraper.scrapers.base import BaseScraper
import wikipedia

from triviascraper.utils import (
    get_first_sentence,
    get_stripped_answer,
    get_stripped_question,
    get_stripped_prefix,
)


class WikipediaScraper(BaseScraper):
    titles = []

    def __init__(self, n_trivias, lang):
        super(WikipediaScraper, self).__init__(n_trivias, lang)
        wikipedia.set_lang(lang)
        self.titles = self.get_random_titles()

    def get_random_titles(self):
        """Return a list of random Wikipedia titles.

        Wikipedia random page API fetches at most 500 titles.
        We use sets to prevent duplicates when sending requests repeatedly.
        """
        titles = set()
        amount = 0
        while amount < self.n_trivias:
            missing = self.n_trivias - amount
            titles = titles.union(set(wikipedia.random(pages=missing)))
            amount = len(titles)
        return titles

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
        """Get first sentence of the summary and remove answer from it."""
        first_sentence = get_first_sentence(article.summary)
        locale_class = get_locale_class(self.locale)
        try:
            question = get_stripped_question(
                article.title, first_sentence.group(), locale_class
            )
        except AttributeError:
            # first_sentence is None
            question = get_stripped_question(
                article.title, article.summary, locale_class
            )
        return {
            "question": question,
            "answer": get_stripped_answer(article.title),
            "categories": [
                get_stripped_prefix(cat, locale_class.strip_category_prefix)
                for cat in article.categories
                if not cat.startswith(locale_class.block_category_prefix)
            ],
            "locale": self.locale,
        }
