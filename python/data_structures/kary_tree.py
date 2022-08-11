from data_structures.queue import Queue

class KaryTree:
    def __init__(self, root=None):
        self.root = root

    def breadth_first(self):
        queue = Queue()

        collection = []

        queue.enqueue(self.root)

        while not queue.is_empty():
            node = queue.dequeue()
            collection.append(node.value)
            for child in node.children:
                queue.enqueue(child)

        return collection

    def clone(self):
        # return a clone of the tree with new nodes keeping the values
        if not self.root:
            return KaryTree()

        origin_queue = Queue()
        clone_queue = Queue()

        clone_root = Node(self.root.value)

        origin_queue.enqueue(self.root)
        clone_queue.enqueue(clone_root)

        while not origin_queue.is_empty():
            front = origin_queue.dequeue()
            clone_front = clone_queue.dequeue()

            for child in front.children:
                origin_queue.enqueue(child)
                clone_node = Node(child.value)
                clone_queue.enqueue(clone_node)
                clone_front.children.append(clone_node)

        return KaryTree(root=clone_root)

class Node:
    """K-Ary Tree Node"""

    def __init__(self, value):
        self.value = value
        self.children = []
