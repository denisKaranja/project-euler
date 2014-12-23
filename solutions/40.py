#!/usr/bin/python
"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics, Chiromo campus
Email: dee.caranja@gmail.com,
Task: 40(Champernowne's constant)
License type: MIT :)
Status: COMPLETED...
"""
import time
startTime = time.clock()

limit = 1000000
product = j =1
new_string = ''
print("Calculating...")
for i in range(1,limit+1):
	new_string += str(i)

for count in range(7):
	product *= int(new_string[j-1])
	j *= 10

print product
print "Run time...{} secs \n".format(round(time.clock() - startTime, 4))