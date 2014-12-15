"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics,
Email: dee.caranja@gmail.com,
Euler project solution = 1(Sum of all numbers divisible by 3 and 5 in range(1000))
Status: COMPLETED...
"""
#One line code
print sum([x for x in range(1000) if x%3==0 or x%5==0])