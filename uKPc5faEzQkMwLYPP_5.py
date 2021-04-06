
def end_corona(recovers, new_cases, active_cases):
  return round(active_cases / (recovers - new_cases)+0.5)

