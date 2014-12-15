#!/usr/bin/python
"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics, Chiromo campus
Email: dee.caranja@gmail.com,
Task: 104(A fibonacci number that has the first and last pandigit numbers i.e 1-9 in both ends)
License type: MIT :)
Status: PENDING...
"""
import time
startTime = time.clock()

def iterrative_fibo(num):
	x = i = 0
	y = z = 1
	for i in xrange(0, num+1):
		x = y
		y = z
		z = x + y
	return x
def last_9_list(fibo):
	x = iterrative_fibo(fibo)
	answer = str(x).replace("","-").split("-")
	answer = answer[1:len(answer)-1]

	last_nine = str(answer[-9:])
	first_nine = str(answer[0:9])
	#convert from list to string
	char_to_remove = ["'", "[", "]", ", "]
	for char in char_to_remove:
		if char in last_nine or char in first_nine:
			last_nine = last_nine.replace(char, "")
			first_nine = first_nine.replace(char, "")

		#add the numbers up
	#sorted_last_nine = sorted([l for l in last_nine])
	#sorted_first_nine = sorted([f for f in first_nine])
	[a, b] = [first_nine, last_nine]
	return [a, b]

match = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
fibo = 100
print "Calculating..."
while True:
	if not all(k in last_9_list(fibo)[0] for k in match):
		fibo += 1
	elif not all(j in last_9_list(fibo)[1] for j in match):
		fibo += 1
	else:
		break
 
print "Fibo num is {}".format(fibo+1)
run_time = time.clock() - startTime
print "\tRun time... %.5f(secs) or %.5f(mins)" % (run_time, (run_time / 60.0))
