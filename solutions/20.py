#Author: Denis Karanja,
#School of Computing and Informatics,
#The University of Nairobi,
#dee.caranja@gmail.com
#Euler project solution = 20(Sum of factorial)
def factorial(number):
	if number == 1 or number == 0:
		return 1
	else:
		return number * factorial(number - 1)

digitSum = 0
fact = str(factorial(100))

for digit in fact:
	digitSum += int(digit)

print digitSum

#print sum(map(int,str(factorial(100)))) ----> this one iterates and add up the numbers as well