#Author: Denis Karanja,
#Institution: The University of Nairobi, Kenya,
#Department: School of Computing and Informatics,
#Email: dee.caranja@gmail.com,
#Euler project solution = 20(Sum of factorial(100) digits eg 5! = 120 there4 1+2+0=3)
def factorial(number):
	if number == 1 or number == 0:
		return 1
	else:
		return number * factorial(number - 1)

print sum([int(x) for x in str(factorial(100))])

#print sum(map(int,str(factorial(100)))) #----> this one iterates and add up the numbers as well