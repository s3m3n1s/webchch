from typing import NamedTuple
from extractor.extractor import Extractor

from analyzer.analyzers.analyzer_interface import AnalyzerABC
from analyzer.analyzers.wad import Wad
from analyzer.analyzers.whatweb import WhatWeb
from analyzer.analyzers.custom import Custom


# simple to see names
class UtilsNames(NamedTuple):
    Util1 = "Wad"
    Util2 = "WhatWeb"
    Util0 = "Custom"


class Analyzer:
    def __init__(self, analyze_util: str):
        self.util_name = analyze_util
        self.util_worker = Custom()

        self._set_util_worker()

    def _set_util_worker(self):
        if self.util_name == "Wad":
            self.util_worker = Wad()
        elif self.util_name == "WhatWeb":
            self.util_worker = WhatWeb()
        else:
            self.util_worker = Custom()

    @staticmethod
    def _get_data_from_url(url: str):
        extractor = Extractor(url=url)

        data = extractor.data
        return data

    def analyze(self, url: str) -> dict:
        # data = self._get_data_from_url(url=url)
        self.util_worker.analyze(url=url)

        result = {}
        return result
