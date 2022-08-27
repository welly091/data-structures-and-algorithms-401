from .linked_list import LinkedList

class Hashtable:
    """
    This class creates a bucket to store the key/value pair data inside a hashtable.
    """

    def __init__(self, size=1024):
        self.buckets = [None] * size
        self.size = size

    def set(self, key, value):
        """
        Create a new data set and store into the bucket.

        :params key: the key for a data set
        :params value: the value for a data set
        :return: none
        """
        index = self.hash(key)
        bucket = self.buckets[index]
        if not bucket:
            bucket = LinkedList()
            self.buckets[index] = bucket

        #Store key/value as a tuple
        key_value_pair = (key, value)
        bucket.insert(key_value_pair)

    def get(self, key):
        """
        Get the value from a given input key.

        :params key: the key for a data set.
        :return : value/none. If value exists, return the value.
        """
        index = self.hash(key)
        bucket = self.buckets[index]
        if not bucket:
            return None

        current = bucket.head
        while current:
            if current.value[0] == key:
                return current.value[1]
            current = current.next
        return None

    def keys(self):
        """
        Gather all the keys in the bucket

        :return : list, a list of keys
        """
        gathered_keys = []
        for bucket in self.buckets:
            if bucket:
                current = bucket.head
                while current:
                    key_value_pair = current.value
                    gathered_keys.append(current.value[0])
                    current = current.next
        return gathered_keys

    def contains(self, key):
        """
        Check if a data set exists based on the given input key.

        :params key: the key in a data set
        :return : boolean
        """
        index = self.hash(key)
        bucket = self.buckets[index]
        if not bucket:
            return False

        # Traverse the linkedlist
        current = bucket.head
        while current:
            key_value_pair = current.value
            if key_value_pair[0] == key:
                return True
            current = current.next
        return False

    def hash(self, key):
        """
        Hash function for turning the key into a hash code for bucket index.

        :params key: the key of a data set
        :return : int, the index for the bucket
        """
        # add ascii values of each char together
        ascii_values = [ord(char) for char in key]
        ascii_sum = sum(ascii_values)

        #Sum multiplied by a prime number
        primed = ascii_sum * 599

        #Devided by the length to get the bucket index
        index = primed % self.size

        return index
