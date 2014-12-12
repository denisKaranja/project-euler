#!/usr/bin/python
#Author: Denis Karanja,
#Institution: The University of Nairobi, Kenya,
#Department: School of Computing and Informatics,
#Email: dee.caranja@gmail.com,
#Problem: Project Euler solution = 22(Names scores. the sum of all names in 22_names.txt).
import time

startTime = time.clock()
print "\nCalculating total name score..."
namesList = ''

file_handler = open("22_names.txt", 'r');

for line in file_handler:
	namesList += line;

namesList = namesList.strip("\n").replace('"', "").split(",")

allNamesSum = 0

for index, name in enumerate(sorted(namesList)):
	nameSum = 0
	alphabets = dict(A = 1,B = 2,C = 3,D = 4,E = 5,F = 6,G = 7,H = 8,I = 9,J = 10,K = 11,L = 12,M = 13,
		N = 14,O = 15,P = 16,Q = 17,R = 18,S = 19,T = 20,U = 21,V = 22,W = 23,X = 24,Y = 25,Z = 26)
	
	for i in name:
		if alphabets.__contains__(i):
			nameSum += alphabets.get(i)

	temp_nameSum = nameSum
	nameSum *= index + 1
	allNamesSum += nameSum

	#print name + " pos "+ str(index+1) +" ->> " + str(temp_nameSum) +" \nTotal count so far is %d * %d == "\
	#% (nameSum, index+1) + str(allNamesSum)+"\n"

print "\tTotal name score ->>", allNamesSum
print "\tProgram took %f seconds to execute\n" % (time.clock() - startTime)





	

	




