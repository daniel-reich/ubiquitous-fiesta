
import collections
​
def sigilize(desire):
  desire=desire.upper()
  d=set()
  s=''
  for x in desire[::-1]:
    if x.isalpha() and x not in 'AEIOU':
      if x not in d:
        s+=x
        d.add(x)
  return s[::-1]

