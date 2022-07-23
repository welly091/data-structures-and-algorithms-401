class LinkedList:
    """
    This is a LinkedList data structure Class is initiated to store Node instances.
    """
    def __init__(self):
        # initialization here
        self.head = None

    def includes(self, val):
        '''
        Check if a Node with target value is in the linkedlist.
        '''
        current = self.head
        while current:
            if current.value == val:
                return True
            current = current.next
        return False

    def insert(self, val):
        '''
        Insert new Node at the front of linkedlist.
        '''
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def append(self, val):
        if not self.head:
            new_node = Node(val)
            new_node.next = self.head
            self.head = new_node
            return
        '''
        Add a new Node at the end of linkedlist.
        '''
        current = self.head
        while current.next != None:
            current = current.next
        current.next = Node(val)

    def insert_before(self, val, new_val):
        '''
        Insert a new Node before an existed Node.
        '''
        if self.head == None:
            raise TargetError()

        # Check the first Node
        if self.head.value == val:
            new_node = Node(new_val)
            new_node.next = self.head
            self.head = new_node
            return

        # Check middle Nodes
        current = self.head
        while current.next and current.next.value != val:
            current = current.next

        # Check the last Node
        if current.next == None and current.value !=val:
            raise TargetError()
        else:
            newNode = Node(new_val)
            newNode.next = current.next
            current.next = newNode

    def insert_after(self, val, new_val):
        '''
        Insert a new Node after an existed Node
        '''
        # If it's an empty linkedlist, raise TargetError
        if self.head == None:
            raise TargetError()
        current = self.head
        while current and current.value != val:
            current = current.next
        if current == None:
            raise TargetError()
        else:
            new_node = Node(new_val)
            temp = current.next
            current.next = new_node
            new_node.next = temp

    def kth_from_end(self, index):
        '''
        Find the nth Node from the end of the linkedlist.
        '''
        #If the index is negative number, raise TargetError()
        if index < 0:
            raise TargetError()

        #Everytime we iterate the linkedlist, we store the value into a list
        current = self.head
        list_val = []
        while current:
            list_val.append(current.value)
            current = current.next

        #If the index is larger than the length of linkedlist, raise TargetError()
        if len(list_val)-1 < index:
            raise TargetError()

        return list_val[len(list_val)-1-index]

    def __str__(self):
        current = self.head
        result = ""
        while current:
            print(current.value)
            result += '{ ' + str(current.value) + ' } -> '
            current = current.next
        result += "NULL"
        return result

class Node:
    """
    A Node Class is used to create a Node instance to store any type of data and the 'next' variable is the reference to another Node instance.
    """
    def __init__(self, value):
        self.value = value
        self.next = None

class TargetError(Exception):
    pass

