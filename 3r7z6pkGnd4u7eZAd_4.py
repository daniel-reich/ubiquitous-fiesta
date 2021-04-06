
def mark_maths(lst):
  lst = [i.replace('=','==') for i in lst]
  return str(round(sum(1 for i in lst if eval(i))*100 /len(lst))) + '%'

