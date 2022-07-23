# Code Challenge Class 05 Linked List Implementation
# Singly Linked List
This code challenge about how to create a Linked List and modify the Node instances inside the list.

## Challenge
All tests for this challenge should be passed.

## Approach & Efficiency
Contruct a Node class and a linked list class. A linked list can be initiated and stored Nodes instances that contains data.
The Big(O) for time complexity for handling a linked list is O(n) where n is determined by the linked list length.
The Big(O) for space complexity is O(1).

## API

[linked_list class](../../data_structures/linked_list.py)
- includes(val): Check if a Node with target value is in the linkedlist.
- insert(val): Insert a new Node at the front of linkedlist.
- append(val): Add a new Node at the end of linkedlist.
- insert_before(a,b): Insert a new Node 'b' before an existed Node 'a'.
- insert_after(a,b): Insert a new Node 'b' after an existed Node 'a'.
- kth_from_end(n): Find the nth Node from the end of the linkedlist.

[linked_list_zip](../../code_challenges/linked_list_zip.py)
- zip_lists(a,b): Merge two linked lists into one linked lists.

## Testing

Go to **[test/code_challenges](../../tests/code_challenges)** folder and run ``pytest`` for each following test module.

[linked_list_insertions](../../tests/code_challenges/test_linked_list_insertions.py)

[linked_list_kth](../../tests/code_challenges/test_linked_list_kth.py)

[linked_list_zip](../../tests/code_challenges/test_linked_list_zip.py)
