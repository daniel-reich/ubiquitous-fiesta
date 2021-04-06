
from collections import Counter
​
def constraint(txt):
  txt1 = ''.join(a.lower() for a in txt if a.isalpha())
  txt4 = ''.join(a.lower() for a in txt if a.isalpha() or a == ' ')
  if len(Counter(txt1)) == 26:
    return 'Pangram'
  elif len(Counter(txt1)) == len(txt1):
    return 'Heterogram'
  else:
    txt2 = [a[0] for a in txt4.split()]
    if len(set(txt2)) == 1:
      return 'Tautogram'
    else:
      txt2 = [set(a) for a in txt4.split()]
      if len(set.intersection(*txt2)) == 1:
        return 'Transgram'
  return 'Sentence'

