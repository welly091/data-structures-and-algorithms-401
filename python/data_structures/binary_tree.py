from data_structures.queue import Queue

class BinaryTree:
    """
    Binary Tree class stores a 'root' Node for the tree and has three methods for traverse.
    """

    def __init__(self):
        self.root = None

    def pre_order(self):
        """
        This method returns a list in a 'pre-order' traverse in Binary Tree.
        :return : list
        """
        pre_order_list = []

        def helper(root):
            if root is None:
                return
            pre_order_list.append(root.value)
            helper(root.left)
            helper(root.right)

        helper(self.root)
        return pre_order_list

    def in_order(self):
        """
        This method returns a list in a 'in-order' traverse in Binary Tree.
        :return : list
        """
        in_order_list = []

        def helper(root):
            if root is None:
                return

            helper(root.left)
            in_order_list.append(root.value)
            helper(root.right)

        helper(self.root)
        return in_order_list

    def post_order(self):
        """
        This method returns a list in a 'post-order' traverse in Binary Tree.
        :return : list
        """
        post_order_list = []

        def helper(root):
            if root is None:
                return

            helper(root.left)
            helper(root.right)
            post_order_list.append(root.value)

        helper(self.root)
        return post_order_list

    def add(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
            return

        q = Queue()
        q.enqueue(self.root)
        while not q.is_empty():
            temp = q.dequeue()
            if temp.left is None:
                temp.left = node
                break
            elif temp.right is None:
                temp.right = node
                break
            else:
                q.enqueue(temp.left)
                q.enqueue(temp.right)

    def find_maximum_value(self):
        """
        Fine the maximum value with those Nodes in a tree.
        :return : int
        """
        if self.root is None:
            return ""

        result = self.root.value
        stack = []
        stack.append(self.root)

        while len(stack) > 0:
            temp = stack.pop()
            result = max(temp.value, result)

            if temp.right:
                stack.append(temp.right)

            temp = temp.left
            while temp:
                if temp:
                    result = max(temp.value, result)
                if temp.right:
                    stack.append(temp.right)
                temp = temp.left

        return result

class Node:
    """
    Node class stores a value and a left child Node and a right child Node.
    """
    def __init__(self, value=None):
        self.value = value
        self.right = None
        self.left = None
