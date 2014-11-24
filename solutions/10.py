#Author: Denis Karanja,
#Institution: The University of Nairobi, Kenya,
#Department: School of Computing and Informatics,
#Email: dee.caranja@gmail.com,
#Euler project solution = 10(Sum of Prime Numbers)

def primeSum(limit):
	for i in str(limit):
		if int(i) % 2 != 0:
			print i
		else:
			print "Prime Number: " + i

print primeSum(100)