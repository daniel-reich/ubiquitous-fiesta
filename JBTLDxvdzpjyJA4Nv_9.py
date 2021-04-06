
from itertools import groupby
​
def super_reduced_string(txt):
  def reduce(sub):
      result = []
      grouped = (list(g) for k, g in groupby(sub))
      for c in grouped:
        if len(c) % 2 == 1:
          result.append(c[0])
      return ''.join(result)
​
  if txt == "":
    return "Empty String"
  temp = reduce(txt)
  return temp if temp == txt else super_reduced_string(temp)

