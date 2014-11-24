#Author: Denis Karanja,
#School of Computing and Informatics,
#The University of Nairobi,
#dee.caranja@gmail.com
#Euler project solution = 16(sum of digits in 2^1000)

def getPow(num, exponent):
	return num ** exponent

digitSum = 0
answer = str(getPow(2, 1000))

for digit in answer:
	digitSum += int(digit)

print digitSum
