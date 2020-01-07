"""
Main script to be run
"""
from triviascraper.io import parse_params
from triviascraper.scrapers.wikipedia import WikipediaScraper

if __name__ == "__main__":
    # Run main logic
    parse_params()
    scraper = WikipediaScraper(2048, "pt")  # TODO: hook in params
    scraper.run()
