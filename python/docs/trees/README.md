# Code Challenge Class 15
# Binary Tree and BST Implementation
This code challenge introduce a binary tree data structure.

## Challenge
Construct a binary tree data structure that contains Nodes which has data, left child Node, and right child Node.
The tree class should has *pre-order*, *in-order*, and *post-order* methods for user to traverse Nodes.
The other data structure, Binary Search Tree, make sure each Node's left child contains smaller value
and each Node's right child contain larger value than their parent Node.

## Approach & Efficiency
#### Node
The Node class stores a value and has left child Node and right child Node.

#### Binary Tree
Construct a class called Tree and this class contain a Node that can store left and right child Nodes.
If should have *pre-order*, *in-order*, and *post-order* methods for user to be able to travese all Nodes

#### Binary Search Tree
BST inherits the BinaryTree class and has *add* and *contains* methods.
The *add* method will add a new Node into the BST and always make sure the right child Node's value is larger than or equals to the parent Node's value
and the left child Node's value is smaller than parent Node's value.
The conains method check whether the 'target' value is in any of Nodes inside BST.


## API
[Binary Tree](../../data_structures/binary_tree.py)
  - pre_order(): return a list of value of each Node in 'pre-order' traverse.
  - in_order(): return a list of value of each Node in 'in-order' traverse.
  - post_order(): return a list of value of each Node in 'post-order' traverse.

[Binary Search Tree](../../data_structures/binary_search_tree.py)
  - add(value): Add new Node into a binary search tree.
  - contains(target): Check whether or not the target is in any of the Nodes.

## Testing
Go to the test folder to find the following tests file and run pytest:

[test_binary_tree](../../tests/data_structures/test_binary_tree.py)

[test_binary_search_tree](../../tests/data_structures/test_binary_search_tree.py)
