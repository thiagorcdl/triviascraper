"""
Main script to be run
"""
from scrapers.wikipedia import WikipediaScraper


def parse_params():
    """Change behavior based on passed options.

    TODO
    """
    return


if __name__ == "__main__":
    # Run main logic
    parse_params()
    scraper = WikipediaScraper(10, 'pt')  # TODO: hook in params
    scraper.run()
