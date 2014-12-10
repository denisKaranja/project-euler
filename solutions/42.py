#!/usr/bin/python
"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics, Chiromo campus
Email: dee.caranja@gmail.com,
Task: 42(Sum of Triangle words) using the formula ->> Tn = 0.5n(n+1)
License type: MIT :)

"""
import time
import math
startTime = time.clock()
print "\nCalculating triangle word score...\n"

def triangle_numbers(nth_term):
	return int((0.5 * nth_term)*(nth_term + 1))

def quadratic(a=1, b=1, c):
	inner = b**2 - 4*1*c
	if inner < 0: return False
	else: 
		inner = math.sqrt(inner)
		x_one = (-b + inner) / (2*a)
		return int(x_one)
quadratic()

word_list = []
fake = ["DENIS", "SKY", "COLIN"]
file_handle = open('p042_words.txt', 'r')

for line in file_handle:
	word_list.append(line)

for index, word in enumerate(fake):
	word_sum = 0
	alphabets = dict(A = 1,B = 2,C = 3,D = 4,E = 5,F = 6,G = 7,H = 8,I = 9,J = 10,K = 11,L = 12,M = 13,
		N = 14,O = 15,P = 16,Q = 17,R = 18,S = 19,T = 20,U = 21,V = 22,W = 23,X = 24,Y = 25,Z = 26)

	for char in word:
		if alphabets.__contains__(char):
			word_sum += alphabets.get(char)

	if word_sum == 55:
		print "\tFound at %d(%s) and is %d" %(index, word, word_sum)
	else:
		print "\t%s ->> %s" % (word, str(word_sum))

print "\nProgram took %f secs to execute\n"%(time.clock() - startTime)
