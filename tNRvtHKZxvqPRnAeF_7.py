
import math
def digit_occurrences(start, end, digit):
  count=0
  for num in range(start,end+1):
    for letter in str(num):
      if letter in str(digit):
        print(digit)
        count+=1
  return count

