import time

startTime = time.clock()

(calls, new_calls) = (0, 0)

def ackermann(m, n):
	global calls
	calls += 1
	if m == 0: 
		return n + 1
	elif m > 0 and n == 0: 
		return ackermann(m-1, 1)
	elif m > 0 and n > 0: 
		return ackermann(m-1, ackermann(m, n-1))

start_full = time.clock()
print "Fully recursive\n{} ({} calls)".format(ackermann(3, 6), calls)
print "{}(secs)".format(time.clock() - start_full)

def iter_ackerman(m, n):
	global new_calls
	new_calls += 1
	while m is not 0:
		if n is 0:
			n = 1
		else:
			n = iter_ackerman(m, n-1)
		m -= 1
	return n +1

start_partial = time.clock()
print "\nPartial recursive\n{} ({} calls)".format(iter_ackerman(3, 6), new_calls)
print "{}(secs)".format(time.clock() - start_partial)