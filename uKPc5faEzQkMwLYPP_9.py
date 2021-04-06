
def end_corona(rec, new, act):
  days = 0
  while act > 0:
    act -= (rec - new)
    days += 1
  return days

