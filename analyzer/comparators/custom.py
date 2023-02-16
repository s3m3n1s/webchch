from analyzer.comparators.comparator_interface import ComparatorABC


class CustomComparator(ComparatorABC):
    def compare(self, data_to_compare_list=list, result_list=list) -> dict:
        pass
