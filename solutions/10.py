#Author: Denis Karanja,
#Institution: The University of Nairobi, Kenya,
#Department: School of Computing and Informatics,
#Email: dee.caranja@gmail.com,
#Euler project solution = 10(Sum of Prime Numbers)
sumOfPrime = 0
number = 0

for i in range(2, 10000):
	if (i % 1 == 0) and (i % i == 0) and (i % 2 is not 0):
		if(i < 9):	
			sumOfPrime += i
			print i
			number += 1
		else:
			if (i % 3 is not 0) and (i % 5 is not 0) and (i % 7 is not 0):
				sumOfPrime += i
				print i
				number += 1

	elif i == 2:
		print i
		sumOfPrime += i
		number += 1

print sumOfPrime
print "This is the %dth prime" % number