
def end_corona(recovers, new_cases, active_cases):
  counter = 0
  dummy = active_cases
  while dummy > 0:
    dummy = dummy + new_cases - recovers
    counter += 1
  return counter

