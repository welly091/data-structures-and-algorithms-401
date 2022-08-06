from data_structures.binary_tree import BinaryTree, Node

class BinarySearchTree(BinaryTree):
    """
    BinarySearchTree class stores Nodes and make sure the left child is always smaller the parent Node
    and right child Node is always larger than or equal to the parent Node.
    """
    def add(self, value):
        """
        Add new Node with value into the Binary Search Tree.
        :params value: the value needs to be stored
        :type value: int/float/str/bool
        :return : None
        """
        node = Node(value)
        if self.root is None:
            self.root = Node(value)
            return
        def walk(root, node_to_add):
            if root is None:
                return
            if node_to_add.value < root.value:
                if root.left is None:
                    # spot is open
                    root.left = node_to_add
                else:
                   walk(root.left, node_to_add)
            else:
                if root.right is None:
                    #spot available
                    root.right = node_to_add
                else:
                    walk(root.right, node_to_add)
        walk(self.root, node)

    def contains(self, target):
        """
        This method checks whether or not the target Node is inside the Binary Search Tree
        :params target: the value needs to be checked
        :type target: int/float/str/bool
        :return :bool
        """
        def walk(root, target):
            if root is None:
                return False

            if root.value == target:
                return True
            if target < root.value:
                return walk(root.left, target)
            else:
                return walk(root.right, target)

        return walk(self.root, target)

