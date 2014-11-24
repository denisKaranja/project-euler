#Author: Denis Karanja,
#Institution: The University of Nairobi, Kenya,
#Department: School of Computing and Informatics,
#Email: dee.caranja@gmail.com,
#Euler project solution = 48(Sum of Self powers i.e 1^1 + 2^2 + 3^3 +...+ 100^100)

def selfPower(num):
	if num == 1:
		return 1
	else:
		return num**num + selfPower(num - 1)

print selfPower(100)
