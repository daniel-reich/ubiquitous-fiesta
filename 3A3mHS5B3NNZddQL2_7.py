
def interview(lst, tot):
  if len(lst)==8 and tot<=120:
    if all([i<=20 for i in lst]) and all([i<=15 for i in lst[:-2]]) and all([i<=10 for i in lst[:-4]]) and all([i<=5 for i in lst[:-6]]):
      return 'qualified'
  return 'disqualified'

