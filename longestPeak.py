# Sample input
array = [ 1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
expected = 6

# Simple test
def test(exepcted, actual):
    if expected == actual:
        print('Working')
    else:
        print('Expected:', expected, 'Actual:', actual)

def longestPeak(array):
	longestPeak = 0
	i = 1
	while i < len(array) - 1:
		isPeak = array[i-1] < array[i] and array[i+1] < array[i]
		if not isPeak:
			i += 1
			continue
		# Accumulate left side
		left = i - 2
		while left >= 0 and array[left] < array[left+1]:
			left -= 1
		# Accumulate right side
		right = i + 2
		while right < len(array) and array[right] < array[right - 1]:
			right += 1
		
		total = right - left - 1
		longestPeak = max(longestPeak, total)
		i = right
	return longestPeak

test(expected, longestPeak(array))
