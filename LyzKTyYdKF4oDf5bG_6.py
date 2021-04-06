
from re import split
def find_longest(s):
  return max(split("\W", s.lower()), key=len)

