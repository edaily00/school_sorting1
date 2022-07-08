class TargetNotFound(Exception):
    """HEY"""


def bin_except(a_list, target):



    first = 0
    last = len(a_list) - 1
    while first <= last:
        middle = (first + last) // 2
        if a_list[middle] == target:
            return middle
        if a_list[middle] > target:
            last = middle - 1
        else:
            first = middle + 1
    raise TargetNotFound




