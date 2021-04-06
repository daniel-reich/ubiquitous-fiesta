
import itertools
def combinator(lst,string=""):
  res = []
  for i in itertools.product(*lst):
    res.append(string.join(i))
  return res

