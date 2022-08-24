from code_challenges.sort_merge import merge_sort

def test_case_1():
    actual = merge_sort([8, 4, 23, 42, 16, 15])
    expect = [4, 8, 15, 16, 23, 42]
    assert  actual == expect

def test_case_2():
    actual = merge_sort([20, 18, 12, 8, 5, -2])
    expect = [-2, 5, 8, 12, 18, 20]
    assert actual == expect

def test_case_3():
    actual = merge_sort([5, 12, 7, 5, 5, 7])
    expect = [5, 5, 5, 7, 7, 12]
    assert actual == expect

def test_case_4():
    actual = merge_sort([2, 3, 5, 7, 13, 11])
    expect = [2, 3, 5, 7, 11, 13]
    assert actual == expect

def test_case_5():
    actual = merge_sort([-2, -8, -7, -1, -11, -25])
    expect = [-25, -11, -8, -7, -2, -1]
    assert actual == expect

def test_case_6():
    actual = merge_sort([1, 0, 0, 0, 0, 0, 0])
    expect = [0, 0, 0, 0, 0, 0, 1]
    assert actual == expect

def test_case_7():
    actual = merge_sort([])
    expect = []
    assert actual == expect
