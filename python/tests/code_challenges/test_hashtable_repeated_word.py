import pytest
from code_challenges.hashtable_repeated_word import first_repeated_word, count_words, get_most_frequent


def test_blank():
    actual = first_repeated_word("")
    expected = None
    assert actual == expected



def test_no_repeat():
    actual = first_repeated_word("nobody here but us chickens")
    expected = None
    assert actual == expected



def test_a_a():
    actual = first_repeated_word("apple apple")
    expected = "apple"
    assert actual == expected



def test_a_b_a():
    actual = first_repeated_word("apple banana apple")
    expected = "apple"
    assert actual == expected



def test_a_b_a_b():
    actual = first_repeated_word("apple banana apple banana")
    expected = "apple"
    assert actual == expected



def test_a_b_b_a():
    actual = first_repeated_word("apple banana banana apple")
    expected = "banana"
    assert actual == expected



def test_ignore_case():
    actual = first_repeated_word("apple banana BANANA apple")
    expected = "banana"
    assert actual == expected



def test_ignore_case_flipped():
    actual = first_repeated_word("apple BANANA banana apple")
    expected = "banana"
    assert actual == expected



def test_punctuation():
    actual = first_repeated_word("apple? BANANA! banana, apple.")
    expected = "banana"
    assert actual == expected



def test_punctuation_joins():
    txt = """
  apple
  apple.apple-apple
  banana
  apple?apple
  banana
  """

    actual = first_repeated_word(txt)
    expected = "banana"
    assert actual == expected

###############
### My Test ###
###############

def test_repeated_in_text_1():
    txt = "Once upon a time, there is this; prince once. "
    actual = first_repeated_word(txt)
    expected = "once"
    assert actual == expected

def test_count_1():
    txt = "Once upon a time, there is this; prince once. "
    actual = count_words(txt)
    expected = 9
    assert actual == expected

def test_count_2():
    txt = ""
    actual = count_words(txt)
    expected = 0
    assert actual == expected

def test_count_3():
    txt = "a a a a a a---a a!a a! a"
    actual = count_words(txt)
    expected = 9
    assert actual == expected

def test_frequent_1():
    txt = "a b c a a b A c a"
    actual = get_most_frequent(txt)
    expexted = ["a", "a", "a", "A", "a"]
    assert actual == expexted

def test_frequent_2():
    txt = "Once twice Twice, once, ONCE, once, OnCe! twIce"
    actual = get_most_frequent(txt)
    expexted = ["Once", "once", "ONCE", "once", "OnCe"]
    assert actual == expexted
