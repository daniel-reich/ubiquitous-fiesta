
from fractions import Fraction
def mixed_number(frac):
  if frac[0] == "-":
    sign = "-"
    frac = frac[1:]
  else:
    sign = ""
  a, b = map(int, frac.split("/"))
  if a == 0:
   return "0"
  i = int(a/b)
  j = Fraction(a,b) - i
  res = sign
  if i != 0:
    res = sign  + str(i)
  if j.numerator == 0:
    return res
  else:
    if i != 0:
      return res + " " + str(j) 
    else:
      return res + str(j)

