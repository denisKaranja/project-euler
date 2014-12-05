"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics,
Email: dee.caranja@gmail.com,
Euler project solution = 3(Largest Prime factor of 600851475143)

"""
import time
startTime = time.clock()

def prime(num):
	if num < 2: return False
	if num % 2 == 0: return num == 2

	division = 3

	while (division * division) <= num:
		if num % division == 0:
			return False
		division += 2
	
	return True
def max(list):
	for i in xrange(len(list)):
		maxNum = list[i]
		if list[i] > maxNum:
			list[i] = maxNum
	return maxNum

number = 13195
output = []
i = 0
while i <= number:
	if prime(i):
		if number % i == 0:
			output.append(i)
			print "Prime num found->> {}".format(i)
	i += 1
print "\nLargest prime factor for %d is %d" % (number, max(output))
print "Program took %.4f secs to execute\n"%(time.clock() - startTime)

numberCopy = 600851475143

