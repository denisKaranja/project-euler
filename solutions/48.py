#Author: Denis Karanja,
#Institution: The University of Nairobi, Kenya,
#Department: School of Computing and Informatics,
#Email: dee.caranja@gmail.com,
#Euler project solution = 48(Sum of Self powers i.e 1^1 + 2^2 + 3^3 +...+ 100^100)
import time

def recursive_self_power(num):
	if num == 1:
		return 1
	else:
		return num**num + selfPower(num - 1)

def iter_self_power(num, list_sum = 0):
	for i in xrange(1, num+1):
		list_sum += i**i
	return list_sum

startTime = time.clock()
a = iter_self_power(1000)
print str(a)[-10:]
print "Program took %f secsonds to execute" % (time.clock() - startTime)