
import itertools
​
def trouble(num1, num2):
  d = ({int(k):len(list(g)) for k,g in itertools.groupby(str(num1))})
  try:
    min_v = list(d.keys())[list(d.values()).index(3)]
  except:
    return False
    
  for k,g in itertools.groupby(str(num2)):
    l = sum(1 for x in list(g))
    if l >= 2 and int(k) == min_v:
      return True
  return False

