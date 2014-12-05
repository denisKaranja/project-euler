"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics,
Email: dee.caranja@gmail.com,
Euler project solution = 2(Even fibonacci number <= 4,000,000)
Status:..COMPELETED
"""

#itterative Fibo
def iterrativeFibo(num):
	x = i = evenSum = 0
	y = z = 1
	limit = 4000000

	for i in range(num+1):
		x = y
		y = z
		z = x + y
		if x % 2 == 0: 
			evenSum += x
		if x > limit: 
			print "Value has exceeded the {} limit. Try a lower number please".format(limit)
			break
	print "Value of current x is {}".format(x)
	return evenSum

print "Sum of even integers is : {}".format(iterrativeFibo(32))
