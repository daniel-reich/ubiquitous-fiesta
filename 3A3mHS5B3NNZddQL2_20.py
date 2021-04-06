
def interview(lst, tot):
  if len(lst) < 8:
    return 'disqualified'
  if lst[0] > 5:
    return 'disqualified'
  if lst[1] > 5:
    return 'disqualified'
  if lst[2] > 10:
    return 'disqualified'
  if lst[3] > 10:
    return 'disqualified'
  if lst[4] > 15:
    return 'disqualified'
  if lst[5] > 15:
    return 'disqualified'
  if lst[6] > 20:
    return 'disqualified'
  if lst[7] > 20:
    return 'disqualified'
  if tot > 120:
    return 'disqualified'
  return 'qualified'

