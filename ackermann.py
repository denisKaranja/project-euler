import time

startTime = time.clock()

def ackermann(m, n):
	if m == 0: return n + 1
	elif m > 0 and n == 0: return ackermann(m-1, 1)
	else: return ackermann(m-1, ackermann(m, n-1))
j = 4
i = 0

for i in range(0, j):
	print "Ackermann (%d, %d) is %d" % (i, j, ackermann(i, j))

print "Program took %.3f secs to execute\n"%(time.clock() - startTime)