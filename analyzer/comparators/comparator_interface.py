from abc import ABC, abstractmethod


class ComparatorABC(ABC):
    @abstractmethod
    def compare(self, data_to_compare_list=list, result_list=list) -> dict:
        pass
