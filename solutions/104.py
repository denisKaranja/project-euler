#!/usr/bin/python
"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics, Chiromo campus
Email: dee.caranja@gmail.com,
Task: 5(A number that is divisible by numbers 1 through 20. eg 2520 is divisible by numbers 1 thru 10)
License type: MIT :)
Status: PENDING...
"""
import time
startTime = time.clock()

def iterrativeFibo(num):
	x = i = 0
	y = z = 1
	for i in xrange(0, num+1):
		x = y
		y = z
		z = x + y
	return x
def sort_list(my_list):
	for index in range(1, len(my_list)):
		value = my_list[index]
		i = index - 1
		while (i >= 0) and (value < my_list[i]):
			my_list[i+1] = my_list[i]
			my_list[i] = value
			i -= 1

	return my_list


last_nine = first_nine = 0
fibo = 540
x = iterrativeFibo(fibo)

answer = str(x).replace("","-").split("-")
answer = answer[1:len(answer)-1]

last_nine = str(answer[-9:])
first_nine = str(answer[0:9])

#convert from list to string
char_to_remove = ["'"]
for char in char_to_remove:
	if char in last_nine or char in first_nine:
		last_nine = last_nine.replace(char, "")
		first_nine = first_nine.replace(char, "")
#add the numbers up
#last_nine = sum([int(digit) for digit in last_nine])
#first_nine = sum([int(digit) for digit in first_nine])

print "Getting the last 9 digits..."
print last_nine
iterrative_time = time.clock() - startTime
print "\tRun time... %.5f(secs) or %.5f(mins)" % (iterrative_time, (iterrative_time / 60.0))
