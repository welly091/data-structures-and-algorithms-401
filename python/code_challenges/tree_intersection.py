from data_structures.binary_tree import BinaryTree

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
