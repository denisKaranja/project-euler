#!/usr/bin/python
"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics, Chiromo campus
Email: dee.caranja@gmail.com,
Task: 188(Hyperexponentiation of a number)
License type: MIT :)
Status: COMPLETED...
"""
import sys
sys.setrecursionlimit(1900)
def exponential(base, expo):
	"""Returns base^^expo"""
	if expo is 1:
		return base
	else:
		return pow(base, exponential(base, (expo-1)), pow(10, 8))

def main():
	return((exponential(1777, 1855)))

if __name__ == "__main__":
	print(main())