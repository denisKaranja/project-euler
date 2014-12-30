#!/usr/bin/python
"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics, Chiromo campus
Email: dee.caranja@gmail.com,
Task: 50(Consecutive prime sum below 1million)
License type: MIT :)
Status: PENDING...
"""
def is_prime(num):
	if num < 2: return False
	if num % 2 == 0: return num == 2

	division = 3

	while (division * division) <= num:
		if num % division == 0: return False
		division += 2
	return True

(primes, primes_sum, cons_primes) = ([], 0, [])

for i in xrange(100):
	if is_prime(i):
		primes.append(i)

for j in primes:
	primes_sum += j
	if is_prime(primes_sum):
		cons_primes.append(j)
		continue
	else:
		primes_sum = 0

print (cons_primes)