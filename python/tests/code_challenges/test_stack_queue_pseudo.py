import pytest
from code_challenges.stack_queue_pseudo import PseudoQueue


def test_exists():
    assert PseudoQueue


def test_enqueue_one():
    pq = PseudoQueue()
    pq.enqueue("apples")
    actual = pq.dequeue()
    expected = "apples"
    assert actual == expected


def test_enqueue_two():
    pq = PseudoQueue()
    pq.enqueue("apples")
    pq.enqueue("bananas")

    actual = pq.dequeue()
    expected = "apples"
    assert actual == expected

    actual = pq.dequeue()
    expected = "bananas"
    assert actual == expected


def test_enqueue_dequeue_enqueue_dequeue():
    pq = PseudoQueue()
    pq.enqueue("apples")
    pq.enqueue("bananas")

    pq.dequeue()

    pq.enqueue("cucumbers")
    pq.enqueue("dates")

    actual = [pq.dequeue(), pq.dequeue(), pq.dequeue()]

    expected = ["bananas", "cucumbers", "dates"]

    assert actual == expected

#My test
def test_enqueque_1():
    pq = PseudoQueue()
    pq.enqueue("A")
    pq.enqueue("B")
    pq.enqueue("C")
    pq.enqueue("D")
    a = pq.dequeue()
    b = pq.dequeue()
    actual = ["A", "B"]
    expected = [a, b]
    assert actual == expected

def test_is_empty_1():
    pq = PseudoQueue()
    expected = pq.is_empty()
    actual = True
    assert actual == expected
