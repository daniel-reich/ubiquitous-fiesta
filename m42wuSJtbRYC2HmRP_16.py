
def largest_exponential(lst):
  import operator
  import math
  l = {i:math.log(i[0])*i[1] for i in lst}
  largest = max(l.items(), key=operator.itemgetter(1))[0]
  return lst.index(largest)+1

