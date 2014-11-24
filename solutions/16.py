#Author: Denis Karanja,
#Institution: The University of Nairobi, Kenya,
#Department: School of Computing and Informatics,
#Email: dee.caranja@gmail.com,
#Euler project solution = 16(sum of digits in 2^1000 eg 2^4 = 16 there4 1+6=7)

def getPow(num, exponent):
	return num ** exponent

digitSum = 0
answer = str(getPow(2, 1000))

for digit in answer:
	digitSum += int(digit)

print digitSum
