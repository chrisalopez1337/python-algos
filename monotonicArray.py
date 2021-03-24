# Sample input
array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
expected = True

# Simple test function
def test(expected, actual):
    if expected == actual:
        print('Working')
    else:
        print('Expected:', expected, 'Actual:', actual)

def isMonotonic(array):

