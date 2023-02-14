from abc import ABC, abstractmethod


class AnalyzerABC(ABC):
    @abstractmethod
    def analyze(self, url=None, frequency=None):
        pass

    @abstractmethod
    def get_last_data(self, url=str) -> dict:
        pass
