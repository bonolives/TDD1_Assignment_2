# TEST FIRST TDD CYCLE 1


# Writing first test
def test1_multiply():
    assert multiply(1, 1) == 1


"""
# writing a multiply function to get test one to pass
def multiply(a, b):
    return a * b
"""


# TEST FIRST TDD CYCLE 2


# writing Second Test
def test2_multiply():
    assert multiply(2, 2) == 4


"""
# Updating the multiply function to pass test 2 but making sure test 1 passes too
def multiply(a, b):
    return a * b
"""

# TEST FIRST TDD CYCLE 3


# Writing third test
def test3_multiply():
    assert multiply(3, 3) == 9


# Updating multiply function to pass the third test and also  making sure not to break test 1 and test 2
def multiply(a, b):
    return a * b
