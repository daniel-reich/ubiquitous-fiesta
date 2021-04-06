
from itertools import permutations
​
def simple_equation(a, b, c):
  the_numbers = permutations((a, b, c))
  
  expressions = '{}+{}=={}', '{}-{}=={}', '{}*{}=={}', '{}/{}=={}'
  
  results = [j.format(*i).replace('==', '=') for i in the_numbers for j in expressions if eval(j.format(*i))]
  
  try:
    return results[0]
  except IndexError:
    return ''

