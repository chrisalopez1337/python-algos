from test import test
array = [2, 1, 5, 2, 3, 3, 4]
expected = 2

# Super simple naive approach
def firstDuplicateValue(array):
    Found = {}
    for x in array:
        if x in Found:
            return x
        else:
            Found[x] = x
    return -1

test(expected, firstDuplicateValue(array))
