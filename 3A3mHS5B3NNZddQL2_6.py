
def interview(lst, tot):
  mins = [5,5,10,10,15,15,20,20,120]
  return 'qualified' if len(lst) == 8 and all(a <= b for a,b in zip(lst+[tot],mins)) else 'disqualified'

