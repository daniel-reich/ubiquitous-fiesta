
from itertools import product
d = { "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz" }
def letters_combinations(digits):
  combos = list(product(*([chr for chr in d[n]] for n in digits)))
  return set(''.join(pair) for pair in combos if len(pair)>0)

