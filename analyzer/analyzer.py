from extractor.extractor import Extractor


class Analyzer:
    def __init__(self, url: str):
        self.url = url

    def get_data_from_url(self):
        extractor = Extractor(url=self.url)

        data = extractor.data
        return data

    def analyze_by_url(self) -> dict:
        data = self.get_data_from_url()

        result = {}
        return result
