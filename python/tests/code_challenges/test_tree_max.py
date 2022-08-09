import pytest
from data_structures.binary_tree import BinaryTree, Node


def test_max_val():
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(30)
    tree.root.right = Node(-7)

    actual = tree.find_maximum_value()
    expected = 30

    assert actual == expected

######################
##     My Tests     ##
######################

def test_mytest_max_1():

    """
    Tree:
                              150
                100                          250
            75          160            200           350
        125  175     300  500       None None      180  None

    """

    tree = BinaryTree()
    tree.root = Node(150)
    tree.root.left = Node(100)
    tree.root.right = Node(250)
    tree.root.left.left = Node(75)
    tree.root.left.right = Node(160)
    tree.root.right.left = Node(200)
    tree.root.right.right = Node(350)
    tree.root.left.left.left = Node(125)
    tree.root.left.left.right = Node(175)
    tree.root.left.right.left = Node(300)
    tree.root.left.right.right = Node(500)
    tree.root.right.right.left = Node(180)
    actual = tree.find_maximum_value()
    expected = 500
    assert actual == expected

def test_mytest_max_2():
    tree = BinaryTree()
    actual = tree.find_maximum_value()
    expected = ""
    assert actual == expected

def test_mytest_max_3():
    """
    Test when all values are negative.
    """
    tree = BinaryTree()
    tree.root = Node(-30)
    tree.root.right = Node(-25)
    tree.root.left= Node(-26)
    tree.root.left.right = Node(-17)
    tree.root.right.left = Node(-5)
    tree.root.right.right = Node(-38)
    actual = tree.find_maximum_value()
    execpected = -5
    assert actual == execpected
