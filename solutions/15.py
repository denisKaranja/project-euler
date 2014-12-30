#!/usr/bin/python
"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics, Chiromo campus
Email: dee.caranja@gmail.com,
Task: 15(Lattice path)
License type: MIT :)
Status: PENDING...
"""
def lattice_path(grid):
	"""Return the number of travesal routes to the bottom right corner"""
	if grid is 1:
		return 2
	else:
		return grid + (2*lattice_path(grid - 1))

print lattice_path(20)