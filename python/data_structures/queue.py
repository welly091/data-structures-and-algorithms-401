from data_structures.invalid_operation_error import InvalidOperationError

class Queue:
    """
    Queue class is a data structure that follows "first in, first out" mechanism for storing and extracting data.
    There are two pointers we need for this data structure: front and rear.
    'Front' always point to the beginning of queue for user to extract Node data.
    'Rear' always point to the last Node data, which is the latest data added to queue
    """

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        '''
        Enqueue add new data into a queue

        :param value: the value you want to add.
        :type value: int/str/bool
        :return: None
        '''
        # edge case:
        new_rear = Node(value)
        if self.rear is None:
            self.rear = new_rear
            self.front = self.rear
        else:
            old_rear = self.rear
            old_rear.next = new_rear
            self.rear = new_rear

    def dequeue(self):
        '''
        Dequeue remove the oldest data from a queue

        :return: None
        '''
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        #remove from front
        old_front = self.front

        #reset from to the 2nd in line
        self.front = self.front.next

        #reset rear if queue is empty
        if self.front is None:
            self.rear = None

        # return the value
        return old_front.value

    def peek(self):
        '''
        Peek method shows the oldest data in a queue but will not remove the data.

        :return: None
        '''
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.front.value


    def is_empty(self):
        '''
        This method check whether the queue is empty.

        :return: bool
        '''
        return self.front is None

class Node:
    '''
    Node class stores data and contains a pointer which points to another Node with data.
    '''
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_
