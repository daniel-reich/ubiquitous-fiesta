
from string import ascii_lowercase as abc
def tweak_letters(txt, lst):
  return "".join([abc[(abc.index(a)+b)%26]for a, b in zip(list(txt), lst)])

