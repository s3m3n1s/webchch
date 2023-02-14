from abc import ABC, abstractmethod


class AnalyzerABC(ABC):
    @abstractmethod
    def analyze(self, url=None, frequency=None):
        pass
