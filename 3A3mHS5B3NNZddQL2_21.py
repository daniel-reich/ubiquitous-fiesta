
def interview(lst, tot):
  limits = [5, 5, 10, 10, 15, 15, 20, 20]
  if len(lst)<8 or tot>120: 
    return 'disqualified'
  return 'qualified' if all(lst[a]<=limits[a] for a in range(8)) else 'disqualified'

