# Define multiply function logic
def multiply(a, b):
    return 1



'''
other ways of writing the multiply function

def multiply(var_a, var_b):
    result = var_a
    for x in range(1, var_b):
        result = result + var_a
    return result



def multiply(a, b):
    ans = 0
    x = 0
    while x < a:
        ans = ans + b
        x = x + 1
    return ans

'''

# Modifying the multiply function to make the tests pass

def multiply(a, b):
    """the function multiplies a and b to give a*b"""
    return a * b
