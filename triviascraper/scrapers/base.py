import requests

from triviascraper.io import write_to_file
from triviascraper.trivia import Trivia


class BaseScraper:
    BLANK = '____'
    URL = ""
    n_trivias = 0
    lang = "en"

    def __init__(self, n_trivias, lang):
        self.n_trivias = n_trivias
        self.lang = lang

    def fetch_article(self, *args, **kwargs):
        """Fetch a single article from the base URL."""
        return requests.get(self.URL, *args, **kwargs)

    @property
    def iterator(self, *args, **kwargs):
        """Define iteration base for fetching the articles."""
        return range(self.n_trivias)

    def fetch_articles(self):
        """Yield list of articles."""
        for i in self.iterator:
            yield self.fetch_article(i)

    def parse_article(self, article):
        """Parse through article text and extract trivia components."""
        raise NotImplementedError

    def write_trivia(self, trivia):
        """Serialize trivia components and save o file."""
        write_to_file(trivia.to_csv())

    def create_trivia_object(self, article):
        """Create an instance of Trivia with parsed data."""
        trivia_data = self.parse_article(article)
        return Trivia(**trivia_data)

    def get_trivias(self, write=False):
        """Get articles and turn them into pieces of trivia."""
        for article in self.fetch_articles():
            if not article:
                continue
            try:
                trivia = self.create_trivia_object(article)
            except ValueError:
                continue
            else:
                if write:
                    self.write_trivia(trivia)
                else:
                    print(trivia)

    def run(self):
        """Run main logic (get and write trivias)."""
        self.get_trivias(write=True)
