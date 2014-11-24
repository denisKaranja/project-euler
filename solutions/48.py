#Author: Denis Karanja,
#School of Computing and Informatics,
#The University of Nairobi,
#dee.caranja@gmail.com
#Euler project solution = 48(Self powers)

def selfPower(num):
	if num == 1:
		return 1
	else:
		
		return num + selfPower(num - 1)

print selfPower(10)
