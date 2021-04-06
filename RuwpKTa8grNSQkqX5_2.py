
import re
from fractions import Fraction
def fractions(decimal):
  digits = re.findall(r'\d+',decimal)
  left = int(digits[0])
  if len(digits) == 2:
    x = 1
    y = pow(10,len(digits[1]))
    left = int(digits[0])
    right = int(digits[0] + digits[1])
  else:
    x = pow(10,len(digits[1]))
    y = pow(10,len(digits[1])+len(digits[2]))
    left = int(digits[0] + digits[1])
    right = int(digits[0] + digits[1] + digits[2])
​
  num = right - left
  den = y - x
  return str(Fraction(num,den))

