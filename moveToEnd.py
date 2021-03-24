# sample input
array = [ 2, 1, 2, 2, 2, 3, 4, 2 ]
to_move = 2
expected = [4, 1, 3, 2, 2, 2, 2, 2]
# Simple testing function
def test(expected, actual):
    if expected == actual:
        print('Working')
    else:
        print('Not working, expected:', expected, 'actual:', actual)

# O(n) solution
def move_element_to_end(array, toMove):
    i = 0
    swap = len(array) - 1
    while i < swap:
        while i < swap and array[swap] == toMove:
            swap -=1
        if array[i] == toMove:
            array[i], array[swap] = array[swap], array[i]
        i += 1
    return array

test(expected, move_element_to_end(array, to_move))
