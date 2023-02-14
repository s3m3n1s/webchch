from analyzer.analyzers.analyzer_interface import AnalyzerABC


class Wad(AnalyzerABC):
    def analyze(self, url=None, frequency=None):
        pass

    def get_last_data(self, url=str) -> dict:
        pass
