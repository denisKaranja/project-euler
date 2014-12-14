#Author: Denis Karanja,
#Institution: The University of Nairobi, Kenya,
#Department: School of Computing and Informatics,
#Email: dee.caranja@gmail.com,
#Euler project solution = 25(The first term in fibonacci to contain 1000digits)

def iterative_fibo(num):
	x = i = evenSum = 0
	y = z = 1
	limit = 4000000

	for i in range(num+1):
		x = y
		y = z
		z = x + y
	return x

print iterative_fibo(5)