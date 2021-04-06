
from string import ascii_lowercase as abc
​
def caesar_cipher(s, k):
  k = k % 26
  alph = abc + abc.upper()
  shifted = abc[k:] + abc[:k] + (abc[k:] + abc[:k]).upper()
  table = s.maketrans(alph, shifted)
  return s.translate(table)

