
def interview(lst, tot):
  meh = [5,5,10,10,15,15,20,20]
  return 'qualified' if all(a<=b for a,b in zip(lst,meh)) and tot<=120 and len(lst)==8 else 'disqualified'

