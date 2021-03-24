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

# Second attempt, trying to get a better than O(n^2) time.
def optimal_smallest_difference(arrayOne, arrayTwo):
    # Sort the arrays for the more optimal algo
    arrayOne.sort()
    arrayTwo.sort()
    # Store solutions and current smallest difference
    currentSmallest = float('inf')
    result = []
    # Set starting pointers
    p1 = 0
    p2 = 0
    # While we still have room to iterate through
    while p1 < len(arrayOne) and p2 < len(arrayTwo):
        val1 = arrayOne[p1]
        val2 = arrayTwo[p2]
        # if the values are equal, this is the smallest distance
        if val1 == val2:
            return [val1, val2]
        # Calculate the difference
        difference = abs(val1 - val2)
        # Check if this is a potential solution
        if difference < currentSmallest:
            currentSmallest = difference
            result = [val1, val2]
        # Check which pointer we need to increment
        if val1 < val2:
            p1 += 1
        else:
            p2 += 1
    # Return solution
    return result

# Test for second attempt
test(expected, optimal_smallest_difference(test_list_one, test_list_two))
