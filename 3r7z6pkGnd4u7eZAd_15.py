
def mark_maths(lst):
  lst = [eval(i.replace('=','==')) for i in lst]
  return str(round(sum(lst)/len(lst)*100)) + '%'

