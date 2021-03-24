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
    direction = None
    i = 0 
    j = 1
    while j < len(array):
        if direction == None:
            if array[j] == array[i]:
                i += 1
                j += 1
                continue
            elif array[i] < array[j]:
                i += 1
                j += 1
                direction = 'Increase'
            else:
                i += 1
                j += 1
                direction = 'Decrease'
        elif direction == 'Increase':
            if array[i] > array[j]:
                return False
            i += 1
            j += 1
        elif direction == 'Decrease':
            if array[i] < array[j]:
                return False
            i += 1
            j += 1
    return True

test(expected, isMonotonic(array))
