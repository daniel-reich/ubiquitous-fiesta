
import math
import random
​
def is_palindrome_possible(txt):
  ret = []
  
  for item in txt:
    if item not in ret: ret.append(item)
    else: continue
  
  fc = 0
  for val in ret:
    if txt.count(val) % 2 == 0: continue
    else: fc += 1
  
  if fc > 1: return False
  else: return True

