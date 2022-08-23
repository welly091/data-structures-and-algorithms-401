def insertion_sort(unsorted_list):
    """
    Implement insertion sorting algorithm in this method.
    :param unsorted_list: the list needs to be sorted
    :type unsorted_list: list
    :return: list
    """
    for i in range(1,len(unsorted_list)):
        j = i - 1
        temp = unsorted_list[i]

        while j >= 0 and temp < unsorted_list[j]:
            unsorted_list[j+1] = unsorted_list[j]
            j-=1
            unsorted_list[j+1] = temp
    return unsorted_list
