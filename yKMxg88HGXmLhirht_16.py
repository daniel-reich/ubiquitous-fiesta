
from string import ascii_lowercase as asc
​
def add_letters(a):
  s = sum(asc.index(l) + 1 for l in a)
  return asc[s % 26 - 1]

