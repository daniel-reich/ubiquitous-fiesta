
def interview(lst, tot):
  if len(lst) != 8:
    return 'disqualified'
  total = 0
  newlist = ['very easy','very easy','easy','easy','medium','medium','hard','hard']
  for i in range(len(lst)):
    if newlist[i] == 'very easy':
      if lst[i] <= 5:
        total += lst[i]
        continue
      else:
        return 'disqualified'
    elif newlist[i] == 'easy':
      if lst[i] <= 10:
        total += lst[i]
        continue
      else:
        return 'disqualified'
    elif newlist[i] == 'medium':
      if lst[i] <= 15:
        total += lst[i]
        continue
      else:
        return 'disqualified'
    elif newlist[i] == 'hard':
      if lst[i] <= 20:
        total += lst[i]
        continue
      else:
        return 'disqualified'
  if tot > 120:
    return 'disqualified'
  return 'qualified'

