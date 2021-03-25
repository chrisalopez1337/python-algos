from test import test
array = [5, 1, 4, 2]
expected = [8, 40, 10, 20]

# First attempt, quick solution
def arrayOfProducts(array):
	products = []
	i = 0
	while i < len(array):
		sum = 1
		# calculate sum of all numbers to the left
		if i != 0:
			j = i-1
			while j >= 0:
				sum *= array[j]
				j -= 1
		# calculate sum of all numbers to the right
		if i != len(array):
			k = i+1
			while k <= len(array) -1:
				sum *= array[k]
				k += 1
		# Add sum to result
		products.append(sum)
		i += 1
	return products
test(expected, arrayOfProducts(array))
