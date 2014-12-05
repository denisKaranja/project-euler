#Author: Denis Karanja,
#Institution: The University of Nairobi, Kenya,
#Department: School of Computing and Informatics,
#Email: dee.caranja@gmail.com,
#Euler project solution = 2(Even fibonacci number <= 4,000,000)

#itterative Fibo
def iterrativeFibo(num):
	x = i = sum = 0
	y = z = 1
	
	for i in range(num+1):
		x = y
		y = z
		z = x + y
		if x % 2 == 0:
			sum += x
	print x
	return sum

print iterrativeFibo(32)

limit = 40
