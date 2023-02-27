"""Utils exercise."""
__author__ = "730331072"


def all(all_list: list[int], number: int) -> bool:
    """Checks if an all integers in a list are the same as a given integer."""
    all_list_index: int = 0
    if len(all_list) == 0:
        return False
    while all_list_index < len(all_list):
        if all_list[all_list_index] != number:
            return False
        else:
            all_list_index += 1 
    return True


def max(max_list: list[int]) -> int:
    """Returns the largest number in a lis."""
    if len(max_list) == 0:
        raise ValueError("max() arg is an empty List")
    max_list_idx: int = 0
    max_int = max_list[max_list_idx]
    while max_list_idx < len(max_list):
        if max_list[max_list_idx] > max_int:
            max_int = max_list[max_list_idx]
        max_list_idx += 1
    return max_int


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Checks if lists are equal."""
    if len(list1) == 0 or len(list2) == 0:
        return False
    if len(list1) == 0 and len(list2) == 0:
        return True
    if len(list1) != len(list2):
        print("Lists are not equal length.")
        return False
    list_idx: int = 0
    while list_idx < len(list1):
        if list1[list_idx] != list2[list_idx]:
            return False
        if list1[list_idx] == list2[list_idx]:
            list_idx += 1
    return True 