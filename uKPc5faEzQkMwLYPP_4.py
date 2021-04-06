
import math
def end_corona(recovers, new_cases, active_cases):
  return math.ceil(active_cases / (recovers - new_cases))

