
from numpy import log
def largest_exponential(lst):
  return 1 + max(range(len(lst)), key = lambda t: log(lst[t][0])*lst[t][1])

