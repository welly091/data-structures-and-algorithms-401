def quick_sort(list, left, right):
    """
    Sort a list using quick sort algorithm.

    :params list: the list that needs to be sorted
    :params left: the left index that is used for comparing the value with the pivot, starting with 0
    :params right: the right index represents the pivot, starting with the last element
    :return: list, sorted list
    """
    if left < right:
        position = partition(list, left, right)
        quick_sort(list, left, position - 1)
        quick_sort(list, position + 1, right)
    return list

def partition(list, left, right):
    pivot = list[right]
    low = left - 1

    for i in range(left, right):
        if list[i] <= pivot:
            low+=1
            swap(list, i, low)
    swap(list, right, low+1)
    return low + 1

def swap(list, i, low):
    temp = list[i]
    list[i] = list[low]
    list[low] = temp
