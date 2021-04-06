
from math import ceil
def end_corona(recovers, new_cases, active_cases):
  return ceil(active_cases/(recovers - new_cases))

