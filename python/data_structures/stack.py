from data_structures.invalid_operation_error import InvalidOperationError

class Stack:
    '''
    Stack is a data structure that follows "First in, last out" mechanism for storing and extracting data.
    There is one pointer that is needed for handling data.
    'Top' is the pointer points to the latest data.
    '''
    def __init__(self):
        self.top = None

    def push(self, value):
        '''
        Push method add new Node with data into a stack.

        :param value: the value you want to add.
        :type value: int/str/bool
        :return: None
        '''
        node=Node(value, self.top)
        self.top = node

    def pop(self):
        '''
        Pop method removes the top Node, which is the latest data, from a stack.

        :return: None
        '''
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        old_top = self.top
        self.top = self.top.next
        return old_top.value

    def peek(self):
        '''
        Peek method will show the top Node's data but does not remove it from a stack.

        :return : None
        '''
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.top.value

    def is_empty(self):
        '''
        This method check whether the stack is empty.

        :return: bool
        '''
        return self.top is None

class Node:
    '''
    Node class stores data and contains a pointer which points to another Node with data.
    '''
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_

