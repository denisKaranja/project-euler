#Author: Denis Karanja,
#Institution: The University of Nairobi, Kenya,
#Department: School of Computing and Informatics,
#Email: dee.caranja@gmail.com,
#Euler project solution = 10(Sum of Prime Numbers)
sumOfPrime = 0

# for i in range(1, 100):
# 	if (i % 1 == 0) and (i % i == 0) and (i % 2 is not 0):
# 		sumOfPrime += i
# 		print i

# 	elif i == 2:
# 		sumOfPrime += i

# print sumOfPrime


def getPrimeSum(limit):
	for i in range(2, limit):
		if i == 2 or i == 3 or i == 5 or i ==7:
			return i + getPrimeSum(i - 1)
		else:
			if (i % 1 == 0) and (i % i == 0) and (i % 2 is not 0):
				global sumOfPrime
				sumOfPrime += i
				return sumOfPrime

print getPrimeSum(10)