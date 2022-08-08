from data_structures.queue import Queue

def breadth_first(tree):
    """
    This method will print out the tree in Breadth-First-Search order.

    :params tree: Tree structure that contains Nodes with data
    :type tree: Object
    :return : List, BFS order of the tree nodes.
    """
    #If the tree is None or the root is None, return an empty list.
    if tree is None or tree.root is None:
        return []

    #Create a Queue to traverse the tree in BST order
    result =[]
    q = Queue()
    q.enqueue(tree.root)
    while not q.is_empty():
        root = q.dequeue()

        result.append(root.value)
        if root.left:
            q.enqueue(root.left)
        if root.right:
            q.enqueue(root.right)
            print(q.is_empty())

    return result









