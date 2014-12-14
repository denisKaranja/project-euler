#!/usr/bin/python
"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics, Chiromo campus
Email: dee.caranja@gmail.com,
Task: 13(sum of all the digits in number)
License type: MIT :)
Status: COMPLETED...
"""

print str(sum([int(x) for x in open("13_nums.dat", 'r')]))[0:10]

