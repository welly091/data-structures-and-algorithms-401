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

class Node:
    """
    Node class stores a value and a left child Node and a right child Node.
    """
    def __init__(self, value=None):
        self.value = value
        self.right = None
        self.left = None
