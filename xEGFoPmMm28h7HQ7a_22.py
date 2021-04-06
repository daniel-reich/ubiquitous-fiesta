
from itertools import product
def letter_combinations(digits):
  dict = {
  "1" : [],
  "2" : ["a","b","c"],
  "3" : ["d","e","f"],
  "4" : ["g","h","i"],
  "5" : ["j","k","l"],
  "6" : ["m","n","o"],
  "7" : ["p","q","r","s"],
  "8" : ["t","u","v"],
  "9" : ["w","x","y","z"]}
  
  lst =  [dict[digit] for digit in digits]
  p = lst[0]
  for i, q in enumerate(lst[1:]):
    p = ["".join(r) for r in product(p,q)]
  return p

