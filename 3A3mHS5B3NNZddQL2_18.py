
def interview(lst, tot):
  times = [5,10,15,20]
  if len(lst) == 8:
    for i in range(len(lst)):
      if lst[i] <= times[i//2]:
        continue
      else:
        return 'disqualified'
    if tot <= 120:
      return 'qualified'
    else:
      return 'disqualified'
  else:
    return 'disqualified'

