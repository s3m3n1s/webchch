from analyzer.analyzers.analyzer_interface import AnalyzerABC


class Custom(AnalyzerABC):
    def analyze(self, url=None):
        pass

    def get_last_data(self, url=str) -> dict:
        pass
