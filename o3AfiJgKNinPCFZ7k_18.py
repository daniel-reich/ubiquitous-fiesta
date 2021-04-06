
from math import ceil
def partition(txt, n):
  return [txt[n*i:n*(i+1)] for i in range(ceil(len(txt) / n))]

