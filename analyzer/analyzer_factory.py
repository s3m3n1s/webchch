from typing import NamedTuple
from extractor.extractor import Extractor
import dictdiffer
from analyzer.analyzers.analyzer_interface import AnalyzerABC
from analyzer.analyzers.wad_analyzer import Wad
from analyzer.analyzers.whatweb_analyzer import WhatWeb
from analyzer.analyzers.custom import Custom
from analyzer.comparators.wad_comparator import WadComparator
from analyzer.comparators.whatweb_comparator import WhatWebComparator
from analyzer.comparators.custom import CustomComparator


# simple to see names
class UtilsNames(NamedTuple):
    Util1 = "Wad"
    Util2 = "WhatWeb"
    Util0 = "Custom"


class Analyzer:
    def __init__(self, analyze_util: str):
        self.util_name = analyze_util
        self.util_worker = Custom()
        self.util_comparator = CustomComparator()
        self.difference = {}
        self._set_util_worker()

    def _set_util_worker(self):
        if self.util_name == "Wad":
            self.util_worker = Wad()
            self.util_comparator = WadComparator()
        elif self.util_name == "WhatWeb":
            self.util_worker = WhatWeb()
            self.util_comparator = WhatWebComparator()
        else:
            self.util_worker = Custom()
            self.util_comparator = WhatWebComparator()

    @staticmethod
    def _get_data_from_url(url: str):
        extractor = Extractor(url=url)

        data = extractor.data
        return data

    def _calculate_difference(self, data_to_compare, result):
        data_to_compare_list = []
        result_list = []

        if type(data_to_compare) == dict and data_to_compare != {}:
            data_to_compare_list = list(data_to_compare.values())[0]
        if type(result) == dict and result != {}:
            result_list = list(result.values())[0]

        self.difference = self.util_comparator.compare(data_to_compare_list, result_list)

    def analyze(self, url: str):
        data_to_compare = self.util_worker.get_last_data(url=url)
        result = self.util_worker.analyze(url=url)

        self._calculate_difference(data_to_compare, result)
