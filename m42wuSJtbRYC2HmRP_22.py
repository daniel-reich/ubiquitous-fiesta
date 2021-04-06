
from math import log
def largest_exponential(lst):
  return max(range(len(lst)), key=lambda i: lst[i][1] * log(lst[i][0])) + 1

