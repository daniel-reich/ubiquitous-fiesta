
import fractions
from functools import reduce
def gcd(lst):
  retLst = reduce(fractions.gcd,lst)
  return retLst

