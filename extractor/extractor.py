from scraper.scraper import Scraper


class Extractor:
    def __init__(self, url: str):
        self.data = Scraper().scrape()

    def extract(self):
        pass
