from data_structures.stack import Stack

class PseudoQueue:
    '''
    This class uses two stacks to work as a queue data structure.
    One stack is initiated for storing data; the other stack is initiated for extracting data.
    '''
    def __init__(self):
        self.enqueue_stack = Stack()
        self.dequeue_stack = Stack()

    def enqueue(self, value):
        '''
        This method adds new data into a queue.

        :param value: the value you want to add.
        :type value: int/str/bool
        :return: None
        '''
        self.enqueue_stack.push(value)

    def dequeue(self):
        '''
        Dequeue method removes the oldest data from a queue.

        :return: None
        '''
        while not self.enqueue_stack.is_empty():
            temp = self.enqueue_stack.pop()
            self.dequeue_stack.push(temp)

        result = self.dequeue_stack.pop()

        while not self.dequeue_stack.is_empty():
            temp = self.dequeue_stack.pop()
            self.enqueue_stack.push(temp)

        return result

    def peek(self):
        '''
        Peek method shows the oldest data in a queue but will not remove the data.

        :return: None
        '''
        while not self.enqueue_stack.is_empty():
            temp = self.enqueue_stack.pop()
            self.dequeue_stack.push(temp)

        result = self.dequeue_stack.peek()

        while not self.dequeue_stack.is_empty():
            temp = self.dequeue_stack.pop()
            self.enqueue_stack.push(temp)

        return result
    def is_empty(self):
        '''
        This method check whether the stack is empty.

        :return: bool
        '''
        return self.enqueue_stack.is_empty()


