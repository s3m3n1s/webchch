from analyzer.comparators.comparator_interface import ComparatorABC
import dictdiffer


class WhatWebComparator(ComparatorABC):
    def compare(self, data_to_compare_list=list, result_list=list):
        difference = ''
        for diff in list(dictdiffer.diff(data_to_compare_list, result_list)):
            action = diff[0]
            name = ''
            changes = ''

            if action == 'change':
                action = 'Scanned data has changed:'
                if isinstance(diff[1], str):
                    name = diff[1]
                else:
                    for i in diff[1]:
                        name += str(i) + '-'
                    name = name[:-1]

                changes = ": " + str(diff[2][0]) + " -> " + str(diff[2][1])

            if action == 'add':
                action = 'Added to scanned data:'
                name = diff[1]

                for change in diff[2]:
                    changes += '\n' + str(change)

            if action == 'remove':
                action = 'Removed from scanned data:'
                name = diff[1]

                for change in diff[2]:
                    changes += '\n' + str(change)

            difference += action + ' ' + str(name) + ' ' + changes
            difference += '\n\n'

        if difference == '':
            difference = 'None'

        return difference
