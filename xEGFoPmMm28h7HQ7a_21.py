
base = []
​
def letter_combinations(digits):
  global base
  conversions = {2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
  output = []
  
  if len(digits) == 1:
    for L in conversions[ int(digits) ]:
      base.append(L)
    Base = base
    base = []
    return Base
    
  else:
    for x in letter_combinations(digits[0]):
      for y in letter_combinations(digits[1:]):
        output.append(x+y)
    return output

