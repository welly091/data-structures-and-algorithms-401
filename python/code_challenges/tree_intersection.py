from data_structures.binary_tree import BinaryTree
from data_structures.hashtable import Hashtable

# This method implements Stack and does not use hashmap #
'''


def tree_intersection(tree_a, tree_b):
    """
    Takes in two trees and return the intersections of two trees
    :params tree_a: tree objects that contains int
    :params tree_b: tree objects that contains int
    :return: list
    """
    if tree_a.root is None or tree_b.root is None:
        return []

    result = []
    stack_a = []
    stack_b = []

    stack_a.append(tree_a.root)
    stack_b.append(tree_b.root)

    while len(stack_a) > 0 and len(stack_b) > 0:
        temp_a = stack_a.pop()
        temp_b = stack_b.pop()
        if temp_a.value == temp_b.value:
            result.append(temp_a.value)

        if temp_a.right and temp_b.right:
            stack_a.append(temp_a.right)
            stack_b.append(temp_b.right)

        temp_a = temp_a.left
        temp_b = temp_b.left
        while temp_a and temp_b:
            if temp_a.value == temp_b.value:
                result.append(temp_a.value)
            if temp_a.right and temp_b.right:
                stack_a.append(temp_a.right)
                stack_b.append(temp_b.right)
            temp_a = temp_a.left
            temp_b = temp_b.left

    return result
'''


#Code Challenge 32
#This method use hashmap.
def tree_intersection(tree_a, tree_b):
    """
    Takes in two trees and return the intersections of two trees

    :params tree_a: tree objects that contains int
    :params tree_b: tree objects that contains int
    :return: list
    """
    hashtable = Hashtable()
    result = []
    add_to_hashtable(hashtable, tree_a.root, tree_b.root)
    for key in hashtable.keys():
        result.append(int(key))
    return result

def add_to_hashtable(hashtable, root_a, root_b):
    """
    Add tree value into a hashtable if both trees have the same value
    :params hashtable: hashtable that stores values
    :params tree_a: tree objects that contains int
    :params tree_b: tree objects that contains int
    :return: None
    """

    if root_a is None or root_b is None:
        return None

    if root_a.value == root_b.value:
        hashtable.set(str(root_a.value), root_b.value)

    add_to_hashtable(hashtable, root_a.left, root_b.left)
    add_to_hashtable(hashtable, root_a.right, root_b.right)

