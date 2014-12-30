#!/usr/bin/python

def max_val(my_list):
	"""Returns a maximum value of a list"""
	return sorted(my_list)[-1]

def min_val(my_list):
	"""Returns a minimum value in a list"""
	return sorted(my_list)[0]
		

a = [6, 4, 9, 36, 65, 30, 67, 3, -1, 90, 2, 5, 6, 8]
print("Max value in {} is {}".format(a, max_val(a)))

print("Min value in {} is {}".format(a, min_val(a)))