#!/usr/bin/python
"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics, Chiromo campus
Email: dee.caranja@gmail.com,
Task: 42(Sum of Triangle words) using the formula ->> Tn = 0.5n(n+1)
License type: MIT :)
Status: COMPLETED
"""
import time
import math
startTime = time.clock()
print "\nCalculating triangle word score...\n"

def triangle_numbers(nth_term):
	return ((0.5 * nth_term)*(nth_term + 1))

def quadratic(c):
	#n^2 + n -2sum = 0
	a = 1
	b = 1
	inner = pow(b, 2) - ((4 * a * c) * -2)
	if inner < 0: 
		return False
	else: 
		sq = math.sqrt(inner)
		x_one = (-b + sq) / (2*a)
		return x_one

word_list = ''
triangle_words = 0
file_handle = open("p042_words.txt", 'r')

for line in file_handle:
	word_list += line

#strip the new line character(\n)and make the string a list
new_list = word_list.strip("\n").replace('"', "").split(",")

for index, word in enumerate(new_list):
	word_sum = 0
	alphabets = dict(A = 1,B = 2,C = 3,D = 4,E = 5,F = 6,G = 7,H = 8,I = 9,J = 10,K = 11,L = 12,M = 13,
		N = 14,O = 15,P = 16,Q = 17,R = 18,S = 19,T = 20,U = 21,V = 22,W = 23,X = 24,Y = 25,Z = 26)

	for char in word:
		if alphabets.__contains__(char):
			word_sum += alphabets.get(char)

	if float(quadratic(word_sum)).is_integer():
		#print "\tFound at %d(%s) and is %d" %(index, word, word_sum)
		triangle_words += 1

print "\t{} triangle words found bro!".format(triangle_words)
print "\tRun time... %f secs to execute\n"%(time.clock() - startTime)
