
from itertools import product as p
def combinator(lst,x=""):
  return [x.join(i) for i in p(*lst)]

