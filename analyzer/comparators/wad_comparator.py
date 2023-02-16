from analyzer.comparators.comparator_interface import ComparatorABC
import dictdiffer


class WadComparator(ComparatorABC):
    def compare(self, data_to_compare_list=list, result_list=list):
        difference = ''
        for diff in list(dictdiffer.diff(data_to_compare_list, result_list)):
            action = diff[0]
            name = ''
            changes = ''

            if action == 'change':
                if isinstance(diff[1], str):
                    name = diff[1]
                else:
                    for i in diff[1]:
                        if not str(i).isdigit():
                            name += str(i) + '-'
                    name = name[:-1]

                changes = ": " + str(diff[2][0]) + " -> " + str(diff[2][1])

                try:
                    difference += action + ' ' + data_to_compare_list[diff[1][0]]["app"] + ' ' + str(name) + ' ' + changes
                except:
                    difference += action + ' ' + str(name) + ' ' + changes

            if action == 'add':
                name = diff[1]

                for change in diff[2]:
                    changes += '\n' + str(change)

                try:
                    difference += action + ' ' + result_list[diff[1][0]]["app"] + ': ' + changes
                except:
                    difference += action + ' ' + str(name) + ' ' + changes

            if action == 'remove':
                name = diff[1]

                for change in diff[2]:
                    changes += '\n' + str(change)

                try:
                    difference += action + ' ' + data_to_compare_list[diff[1][0]]["app"] + ': ' + changes
                except:
                    difference += action + ' ' + str(name) + ' ' + changes

            difference += '\n\n'

        if difference == '':
            difference = 'None'

        return difference

