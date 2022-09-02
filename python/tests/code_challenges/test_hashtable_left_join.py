import pytest
from code_challenges.hashtable_left_join import left_join, right_join


def test_exists():
    assert left_join


def test_left_join_1():
    synonyms = {
        "diligent": "employed",
        "fond": "enamored",
        "guide": "usher",
        "outfit": "garb",
        "wrath": "anger",
    }
    antonyms = {
        "diligent": "idle",
        "fond": "averse",
        "guide": "follow",
        "flow": "jam",
        "wrath": "delight",
    }

    expected = [
        ["diligent", "employed", "idle"],
        ["fond", "enamored", "averse"],
        ["guide", "usher", "follow"],
        ["outfit", "garb", "NONE"],
        ["wrath", "anger", "delight"],
    ]

    actual = left_join(synonyms, antonyms)

    assert actual == expected

def test_left_join_2():
    synonyms = {
        "diligent": "employed",
        "fond": "enamored",
        "guide": "usher",
        "outfit": "garb",
        "wrath": "anger",
    }
    antonyms = {

    }

    expected = [
        ["diligent","employed", "NONE"],
        ["fond", "enamored", "NONE"],
        ["guide", "usher", "NONE"],
        ["outfit", "garb", "NONE"],
        ["wrath", "anger", "NONE"],
    ]

    actual = left_join(synonyms, antonyms)

    assert actual == expected

def test_left_join_3():
    synonyms = {

    }
    antonyms = {
        "diligent": "idle",
        "fond": "averse",
        "guide": "follow",
        "flow": "jam",
        "wrath": "delight",
    }

    expected = [

    ]

    actual = left_join(synonyms, antonyms)

    assert actual == expected

def test_right_join_1():
    synonyms = {
        "diligent": "employed",
        "fond": "enamored",
        "guide": "usher",
        "outfit": "garb",
        "wrath": "anger",
    }
    antonyms = {
        "diligent": "idle",
        "fond": "averse",
        "guide": "follow",
        "flow": "jam",
        "wrath": "delight",
    }

    expected = [
        ["diligent","idle", "employed"],
        ["fond", "averse", "enamored"],
        ["guide", "follow", "usher"],
        ["flow", "jam", "NONE"],
        ["wrath", "delight", "anger"]
    ]

    actual = right_join(synonyms, antonyms)

    assert actual == expected

def test_right_join_2():
    synonyms = {
        "diligent": "employed",
        "fond": "enamored",
        "guide": "usher",
        "outfit": "garb",
        "wrath": "anger",
    }
    antonyms = {

    }

    expected = [
    ]

    actual = right_join(synonyms, antonyms)

    assert actual == expected

def test_right_join_3():
    synonyms = {
        "angry": "annoyed",
        "furious": "heated",
        "warm": "temperate",
        "flash": "glare",
        "perceptive": "insightful",
    }
    antonyms = {
        "angry": "mild",
        "furious": "calm",
        "warm":"freezing",
        "flash": "dullness"
    }

    expected = [
        ["angry","mild", "annoyed"],
        ["furious", "calm","heated"],
        ["warm", "freezing","temperate"],
        ["flash", "dullness","glare"]
    ]

    actual = right_join(synonyms, antonyms)

    assert actual == expected
