#!/usr/bin/python
"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics, Chiromo campus
Email: dee.caranja@gmail.com,
Task: 14(Longest Collatz sequence { n-> n/2(n is even) and n-> 3n+1(n is odd))
License type: MIT :)
Status: PENDING...
"""
def is_odd_even(num):
  """Check if a number is odd or even"""
  if num % 2 is 0:
    return 1#even num
  else:
    return 0#odd num

def even_generator(num):
  """Generates the next num in the sequence if the previous one was even"""
  return num / 2

def odd_generator(num):
  """Generates the next num in the sequence if the previous one was odd"""
  return (3 * num) + 1

def collatz_sequence(num):
  """Return the number that gives the longest chain"""
  sequence, i, temp = [], 0, num
  while True:
    if is_odd_even(num) is 1:#even number
      sequence.append(num)
      num = even_generator(num)
      if num is 1:
        sequence.append(num)
        break
    elif is_odd_even(num) is 0:#odd number
      sequence.append(num)
      num = odd_generator(num)
      if num is 1:
        sequence.append(num)
        break
  return (len(sequence), temp)

def main():
  largest_sequence = []
  for x in xrange(1, 1000000):
    largest_sequence.append(collatz_sequence(x))

  return max(largest_sequence)

if __name__ == "__main__":
  import time
  start = time.clock()
  print "Calculating largest collatz chain..."
  print main()
  print "Run time...{}(secs)".format(round(time.clock() - start, 5))
