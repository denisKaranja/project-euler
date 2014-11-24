#Author: Denis Karanja,
#School of Computing and Informatics,
#The University of Nairobi,
#dee.caranja@gmail.com
#Euler project solution = 10(Sum of Prime Numbers)

def primeSum(limit):
	for i in str(limit):
		if int(i) % 2 != 0:
			print i
		else:
			print "Prime Number: " + i

print primeSum(100)