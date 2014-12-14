#!/usr/bin/python
"""
Author: Denis Karanja,
Institution: The University of Nairobi, Kenya,
Department: School of Computing and Informatics, Chiromo campus
Email: dee.caranja@gmail.com,
Task: 17(Number letter counts)
License type: MIT :)
Status: COMPLETED...
"""

below_twenty = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
above_twenty = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
word_sum = 0

def number_to_word(num):
  if num == 0:
    return ""
  if num < 20:
    return (below_twenty[num])
  elif num < 100:
    ray = divmod(num,10)
    return (above_twenty[ray[0]-2]+" "+number_to_word(ray[1]))
  elif num <1000:
    ray = divmod(num,100)
    if ray[1] == 0:
        mid = " hundred"
    else:
        mid =" hundred and "
    return(below_twenty[ray[0]]+mid+number_to_word(ray[1]))
  elif num == 1000:
    return "One thousand"

for i in xrange(1, 1001):
  word_sum += len(number_to_word(i).replace(" ", ""))

print word_sum
