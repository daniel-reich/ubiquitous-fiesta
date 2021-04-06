
def end_corona(recovers, new_cases, active_cases):
  a = recovers-new_cases
  days = active_cases/a
  pos = str(days).find(".")
  if str(days)[pos+1:] == 0:
    days = days
  else:
    days += 1 
    days = days - (days-int(str(days)[:pos]))
  return days

