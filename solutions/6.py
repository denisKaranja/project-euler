#Author: Denis Karanja,
#Institution: The University of Nairobi, Kenya,
#Department: School of Computing and Informatics,
#Email: dee.caranja@gmail.com,
#Euler project solution = 6(Sum square difference)

def sumOfSquares(num):
	if num == 1:
		return 1
	else:
		return num**2 + sumOfSquares(num - 1)

def squareOfSums(num):
	if num == 1:
		return 1
	else:
		return num + squareOfSums(num - 1)

a = sumOfSquares(100)
b = squareOfSums(100)**2

diff = a - b
print abs(diff)
