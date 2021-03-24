test_list_one = [-1, 5, 10, 20, 28, 3]
test_list_two = [26, 134, 135, 15, 17]
expected = [28, 26]

# Simple test function
def test(expected, actual):
    if expected == actual:
        print('Working')
    else:
        print('Not working, expected:', expected, 'actual:', actual)

# My first attempt, just a simple brute force, O(n^2) time.
def smallest_difference(arrayOne, arrayTwo):
	result = []
	smallest = float('inf')
	for x in arrayOne:
		for y in arrayTwo:
			distance = abs(x - y)
			if distance < smallest:
				smallest = distance
				result = [x, y]
	return result

# test for O(n^2)
test(expected, smallest_difference(test_list_one, test_list_two))
