
import fractions, functools
def gcd(lst):
  return functools.reduce(fractions.gcd, lst)

