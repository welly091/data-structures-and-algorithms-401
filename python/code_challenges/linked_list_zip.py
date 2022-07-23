from data_structures.linked_list import LinkedList

def zip_lists(a, b):
    """
    This method will merge two linked lists into one linked lists.
    """
    zip_linkedList = LinkedList()
    current_a = a.head
    current_b = b.head
    while current_a and current_b:
        zip_linkedList.append(current_a.value)
        zip_linkedList.append(current_b.value)
        current_a = current_a.next
        current_b = current_b.next
    #If a still have values, iterate the list
    while current_a:
        zip_linkedList.append(current_a.value)
        current_a = current_a.next
    #If b still have values, iterate the list
    while current_b:
        zip_linkedList.append(current_b.value)
        current_b = current_b.next
    return zip_linkedList

