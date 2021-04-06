
from math import exp
​
def salt(t):
  return round(1+9*exp(-0.1*t),3)

