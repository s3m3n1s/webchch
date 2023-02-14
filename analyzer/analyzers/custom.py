from analyzer.analyzers.analyzer_interface import AnalyzerABC


class Custom(AnalyzerABC):
    def analyze(self, url=None, frequency=None):
        pass
