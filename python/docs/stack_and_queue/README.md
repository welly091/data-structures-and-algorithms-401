# Code Challenge Class 10
# Stack and a Queue Implementation
This code challenge introduce two data structures- stack and queue.

## Challenge
Use Node as data storage and have stack and queue to store multiple Nodes. Write methods for both data structures, stack and queue, to add, delete, or show Node's data.

## Approach & Efficiency
#### Stack
Construct a Node class that contains data and a stack class that stores multiple Node instances. The stack class contains push, pop, peek, and is_empty methods.
#### Queue
Construct a Node class that contains data and a queue class that stores multiple Node instances. The queue class contains enqueue, dequeue, peek, and is_empty methods.

All methods in both stack and queue has time complexity O(1).

## API
[Stack](../../data_structures/stack.py)
  - push() : Add new Node into the stack.
  - pop() : Remove the top of Node from the stack.
  - peek() : Show top of Node's data from the stack, but will not be removed.
  - is_empty() : Check if the stack is empty.

[Queue](../../data_structures/queue.py)
  - enqueue() : Add new Node into the queue.
  - dequeue() : Remove the first Node from the queue.
  - peek() : Show the first Node from the queue, but will not be removed.
  - is_empty() : Check if the queue is empty.
