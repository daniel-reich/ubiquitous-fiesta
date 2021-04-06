
from re import findall
def has_digit(txt):
  return any(findall("\d", txt))

