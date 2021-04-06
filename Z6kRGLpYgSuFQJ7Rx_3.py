
from re import split
def find_longest(sentence):
  return max(split("\W", s.lower()), key = len)

