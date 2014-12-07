"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics,
Email: dee.caranja@gmail.com,
Euler project solution = 7(the 10 001st prime number)
Status:...COMPLETED:)
"""
import time
startTime = time.clock()
print "Calculating..."
def prime(num):
	if num < 2: return False
	if num % 2 == 0: return num == 2

	division = 3

	while (division * division) <= num:
		if num % division == 0: return False
		division += 2
	return True

limit = 1000000
print (filter(prime, range(limit)))[10000]
print "Program took %.4f secs to execute\n"%(time.clock() - startTime)
