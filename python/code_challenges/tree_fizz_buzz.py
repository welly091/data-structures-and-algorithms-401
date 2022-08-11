from data_structures.binary_tree import BinaryTree
from data_structures.kary_tree import KaryTree, Node
from data_structures.queue import Queue

def fizz_buzz_tree(tree):
    """
    Return a new k-ary tree that contains desired "FizzBuzz" values if the value in each node
    is divisible by 15, 3, or 5.

    :params tree: The original k-ary tree
    :type tree: k-ary Tree Object
    :return: k-ary Tree object
    """
    new_tree = tree.clone()

    def helper(node):
        if node.value % 15 == 0:
            node.value = "FizzBuzz"
        elif node.value % 3 == 0:
            node.value = "Fizz"
        elif node.value % 5 == 0:
            node.value = "Buzz"
        else:
            node.value = str(node.value)
        return node

    queue = Queue()
    new_tree.root = helper(new_tree.root)
    queue.enqueue(new_tree.root)
    while not queue.is_empty():
        node = queue.dequeue()
        for child in node.children:
            child = helper(child)
            queue.enqueue(child)

    return new_tree
