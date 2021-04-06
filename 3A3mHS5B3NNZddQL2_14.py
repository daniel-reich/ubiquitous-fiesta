
def interview(lst, tot):
  allowed = [5,5,10,10,15,15,20,20]
  if len(lst) == 8:
    if tot <= 120:
      if all(a<=b for a,b in zip(lst, allowed)):
        return 'qualified'
  return 'disqualified'

