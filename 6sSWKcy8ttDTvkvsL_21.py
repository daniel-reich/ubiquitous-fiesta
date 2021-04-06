
def after_n_days(days, n):
  wdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                'Friday', 'Saturday', 'Sunday']
  out = []
  for day in days:
    new_id = wdays.index(day) + n
    while new_id > 6:
      new_id -= 7
    out.append(wdays[new_id])
  
  return out

