# TEST FIRST TDD CYCLE 1

from multiply import multiply

# Writing first test
def test1_multiply():
    """ function multiplies 1 by 1 to give 1 """
    assert multiply(1, 1) == 1


'''
# writing a multiply function to get test one to pass
def multiply(a, b):
    return a * b
'''

# TEST FIRST TDD CYCLE 2


# writing Second Test
def test2_multiply():
    """ the function multiplies 2 by 2 to give 4 """
    assert multiply(2, 2) == 4


'''
# Updating the multiply function to pass test 2 but making sure test 1 passes too
def multiply(a, b):
    return a * b
'''

# TEST FIRST TDD CYCLE 3


# Writing third test
def test3_multiply():
    """ the function multiplies 3 by 3 to give 9 """
    assert multiply(3, 3) == 9


'''
# Updating multiply function to pass the third test and also  making sure not to break test 1 and test 2
def multiply(a, b):
    return a * b
'''

# FOURTH TEST CYCLE


# Writing test four : Its Red
def test4_multiply():
    """ the function multiplies 4 by 4 to give 16 """
    assert multiply(4, 4) == 16


'''
# Making fourth test cycle green
def multiply(a, b):
    return a * b
'''

# FIFTH TEST CYCLE


# writing fifth test: it's Red
def test5_multiply():
    # assert multiply(23, 45) == 23 * 45 
    """ the function multiplies 23 by 45 to give 1035""" 

    assert multiply(23,45) == 1035

# docstring help define func params, return values, (Read about them)
# With the test instead of writing (23*45) its better to put calculator value as result

# END OF ASSIGNMENT
