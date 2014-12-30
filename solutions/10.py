"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics,
Email: dee.caranja@gmail.com,
Euler project solution = 10(Sum of Prime Numbers)
Status:...COMPLETED

"""
import time
print "Calculating..."
def prime(num):
	if num < 2: 
		return False
	if num % 2 == 0: 
		return num == 2

	start_point = 3

	while (start_point * start_point) <= num:
		if num % start_point == 0:
			return False
		start_point += 2
	return True

limit = 2000000
startTime = time.clock()
print "sum is ->> {}".format(sum(filter(prime, xrange(1, limit))))
print "Run time... {}".format(round(time.clock() - startTime, 5))