
from re import *
def remove_leading_trailing(n):
  n = findall(r"^0*(\d+(?:\.(?:(?!0+$)\d)+)?)",n)
  return n[0]

