
from string import ascii_lowercase as al
def nearest_vowel(s):
  return sorted((abs(al.index(s)-al.index(c)),c) for c in 'aeiou')[0][1]

