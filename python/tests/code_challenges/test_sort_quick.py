from code_challenges.sort_quick import quick_sort

def test_case_1():
    actual = quick_sort([8, 4, 23, 42, 16, 15], 0, 5)
    expect = [4, 8, 15, 16, 23, 42]
    assert  actual == expect

def test_case_2():
    actual = quick_sort([20, 18, 12, 8, 5, -2], 0, 5)
    expect = [-2, 5, 8, 12, 18, 20]
    assert actual == expect

def test_case_3():
    actual = quick_sort([5, 12, 7, 5, 5, 9, 7], 0, 6)
    expect = [5, 5, 5, 7, 7, 9, 12]
    assert actual == expect

def test_case_4():
    actual = quick_sort([2, 3, 5, 7, 13, 11, 28], 0,6)
    expect = [2, 3, 5, 7, 11, 13, 28]
    assert actual == expect

def test_case_5():
    actual = quick_sort([-2, -8, -7, -1, -11, -25], 0, 5)
    expect = [-25, -11, -8, -7, -2, -1]
    assert actual == expect

def test_case_6():
    actual = quick_sort([1, 0, 0, 0, 0, 0, 0], 0,6)
    expect = [0, 0, 0, 0, 0, 0, 1]
    assert actual == expect

def test_case_7():
    actual = quick_sort([], 0, 0)
    expect = []
    assert actual == expect

def test_case_8():
    actual = quick_sort([5,4,3,2,1], 0, 4)
    expect = [1,2,3,4,5]
    assert actual == expect
