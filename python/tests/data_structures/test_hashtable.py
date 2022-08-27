import pytest
from data_structures.hashtable import Hashtable


def test_exists():
    assert Hashtable


def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected


def test_internals():
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")

    actual = []

    # NOTE: purposely breaking encapsulation to test the "internals" of Hashmap
    for item in hashtable.buckets:
        if item:
            result = []
            current = item.head
            while current:
                result.insert(0, list(current.value))
                current = current.next
            actual.append(result)
    expected = [[["silent", True], ["listen", "to me"]], [["ahmad", 30]]]

    assert actual == expected

####################
##### My Tests #####
####################

#Test for checking if a key exist inside a hashtable
def test_contains_key_1():
    hashtable = Hashtable()
    hashtable.set("a", 10)

    expected = True
    actual = hashtable.contains("a")
    assert actual == expected

#Test for checking if a key exist inside a hashtable
def test_contains_key_2():
    hashtable = Hashtable()
    hashtable.set("b", 10)

    expected = False
    actual = hashtable.contains("a")
    assert actual == expected

## Test for key does not exist inside the hashtable
def test_contains_key_3():
    hashtable = Hashtable()

    expected = None
    actual = hashtable.get("a")
    assert actual == expected

## Test for retrieving all data that has the same key
def test_keys_values_1():
    hashtable = Hashtable()
    hashtable.set("a", 10)
    hashtable.set("a", 11)
    hashtable.set("a", 12)
    hashtable.set("a", 13)
    hashtable.set("a", 14)
    hashtable.set("b", 20)
    hashtable.set("c", 30)
    hashtable.set("d", 40)
    hashtable.set("e", 50)

    actual = []
    for item in hashtable.buckets:
        if item and item.head.value[0] == "a":
            current = item.head
            while current:
                actual.append(current.value)
                current = current.next
    expected = [("a", 14),("a", 13),("a", 12),("a", 11),("a", 10)]

    assert actual == expected

#Test for checking hash collision
def test_same_hashcode_1():
    hashtable = Hashtable()
    assert hashtable.hash("Ah") == hashtable.hash("Bg")

# Test for retrieving all data that has the same hash code
def test_same_hashcode_2():
    hashtable = Hashtable()

    #The following key/value should have same hashcode
    hashtable.set("Ah", 10)
    hashtable.set("Bg", False)
    hashtable.set("Cf", "WOW")

    #The hashcode for "Ah" should be as same as "Bg" and "Cf
    the_index = hashtable.hash("Ah")

    actual = []
    current = hashtable.buckets[the_index].head
    while current:
        actual.append(current.value)
        current = current.next

    expected = [("Cf", "WOW"), ("Bg", False), ("Ah", 10)]
    assert actual == expected

#Test for retrieving the wanted value based on a given key
def test_get_value_1():
    hashtable = Hashtable()
    hashtable.set("a", 10)
    hashtable.set("b", 20)
    hashtable.set("c", 30)
    hashtable.set("d", 40)
    hashtable.set("e", 50)

    actual = hashtable.get("c")
    expected = 30
    assert actual == expected

# Test for retrieving a value from a bucket within the hashtable that has a collision
def test_get_value_2():
    hashtable = Hashtable()
    hashtable.set("Ah", 10)
    hashtable.set("Bg", False)
    hashtable.set("Cf", "WOW")

    actual = hashtable.get("Bg")
    expected = False
    assert actual == expected
