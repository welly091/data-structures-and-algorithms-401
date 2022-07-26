import pytest
from data_structures.linked_list import LinkedList, TargetError


def test_append():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    linked_list.append("cucumber")

    assert str(linked_list) == "{ banana } -> { apple } -> { cucumber } -> NULL"


def test_insert_before():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    linked_list.insert_before("apple", "cucumber")

    assert str(linked_list) == "{ banana } -> { cucumber } -> { apple } -> NULL"


def test_insert_before_first():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert_before("apple", "cucumber")

    assert str(linked_list) == "{ cucumber } -> { apple } -> NULL"


def test_insert_after():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    linked_list.insert_after("banana", "cucumber")

    assert str(linked_list) == "{ banana } -> { cucumber } -> { apple } -> NULL"



def test_insert_before_empty():
    linked_list = LinkedList()

    with pytest.raises(TargetError):
        linked_list.insert_before("radish", "zucchinni")


def test_insert_before_missing():
    linked_list = LinkedList()

    linked_list.insert("banana")

    with pytest.raises(TargetError):
        linked_list.insert_before("radish", "zucchinni")


def test_insert_after_empty():
    linked_list = LinkedList()

    with pytest.raises(TargetError):
        linked_list.insert_after("radish", "zucchinni")


def test_insert_after_missing():
    linked_list = LinkedList()

    linked_list.insert("banana")

    with pytest.raises(TargetError):
        linked_list.insert_after("radish", "zucchinni")


'''
######################################################
Strech goal
Delete tests
######################################################
'''

def test_delete_head():
    link_list = LinkedList()
    link_list.insert("John")
    link_list.insert("Karen")
    link_list.insert("Dan")
    link_list.insert("Polo")

    link_list.delete("Polo")
    assert str(link_list) == "{ Dan } -> { Karen } -> { John } -> NULL"

def test_delete_middle_1():
    link_list = LinkedList()
    link_list.insert("John")
    link_list.insert("Karen")
    link_list.insert("Dan")
    link_list.insert("Polo")

    link_list.delete("Dan")
    assert str(link_list) == "{ Polo } -> { Karen } -> { John } -> NULL"

def test_delete_middle_2():
    link_list = LinkedList()
    link_list.insert("John")
    link_list.insert("Karen")
    link_list.insert("Dan")
    link_list.insert("Polo")

    link_list.delete("Karen")
    assert str(link_list) == "{ Polo } -> { Dan } -> { John } -> NULL"

def test_delete_last():
    link_list = LinkedList()
    link_list.insert("John")
    link_list.insert("Karen")
    link_list.insert("Dan")
    link_list.insert("Polo")

    link_list.delete("John")
    assert str(link_list) == "{ Polo } -> { Dan } -> { Karen } -> NULL"

def test_delete_twice():
    link_list = LinkedList()
    link_list.insert("John")
    link_list.insert("Karen")
    link_list.insert("58")
    link_list.insert("Polo")

    link_list.delete("John")
    link_list.delete("Karen")
    assert str(link_list) == "{ Polo } -> { 58 } -> NULL"

def test_delete_error():
    link_list = LinkedList()
    link_list.insert("John")
    link_list.insert("Karen")
    link_list.insert("58")
    link_list.insert("Polo")

    link_list.delete("John")


    with pytest.raises(TargetError):
        link_list.delete("John")
