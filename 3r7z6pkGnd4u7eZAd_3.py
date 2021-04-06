
def mark_maths(lst):
  return str(round((sum(1 for i in lst if eval(i.replace('=','=='))) / len(lst))*100)) + '%'

