
from math import ceil
def legalbacklog(cases, max_daily_sessions):
  return max(max(cases.values()), ceil(sum(cases.values())/max_daily_sessions))

