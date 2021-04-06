
from math import ceil
def legalbacklog(cases, max_sess):
  vals = cases.values()
  return max(max(vals), ceil(sum(vals)/max_sess))

