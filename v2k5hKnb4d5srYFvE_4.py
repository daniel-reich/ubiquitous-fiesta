
from itertools import product as PD 
def letters_combinations(digits):
  d = { "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz" }
  A=[d[x] for x in digits]
  if len(digits)>0:
    return {''.join(list(x)) for x in PD(*A)}
  else:
    return set()

