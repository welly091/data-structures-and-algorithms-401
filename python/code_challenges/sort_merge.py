def merge_sort(unsorted_list):
    """
    Takes in an unsorted list as an argument and use merge sort algorithm to sort the list.

    :param unsorted_list: list.
    :return: list, sorted.
    """
    list_length = len(unsorted_list)
    if list_length > 1:
        mid = list_length // 2
        left = unsorted_list[0:mid]
        right = unsorted_list[mid:list_length]

        merge_sort(left)
        merge_sort(right)
        Merge(left, right , unsorted_list)
    return unsorted_list

def Merge(left, right, unsorted_list):
    """
    A helper method for merge_sort method that sort sub-lists.

    :param left: list, first half list
    :param right: list, second half list
    :param unsorted_list:list, origin list
    :return: None
    """
    left_index, right_index, list_index = 0, 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            unsorted_list[list_index] = left[left_index]
            left_index += 1
        else:
            unsorted_list[list_index] = right[right_index]
            right_index += 1
        list_index+=1

    while left_index < len(left):
        unsorted_list[list_index] = left[left_index]
        left_index+=1
        list_index +=1
    while right_index < len(right):
        unsorted_list[list_index] = right[right_index]
        right_index += 1
        list_index += 1
