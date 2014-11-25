#Author: Denis Karanja,
#Institution: The University of Nairobi, Kenya,
#Department: School of Computing and Informatics,
#Email: dee.caranja@gmail.com,
#Euler project solution = 2(Even fibonacci number <= 4,000,000)

evenSum = 0
def fibo(num):
	if num  <= 0 or num == 1:
		return 1
	else:
		return fibo(num - 1) + fibo(num - 2) 

print fibo(30)