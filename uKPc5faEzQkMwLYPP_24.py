
def end_corona(recovers, new_cases, active_cases):
  return active_cases // (recovers - new_cases) + 1

