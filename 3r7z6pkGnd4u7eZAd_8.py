
def mark_maths(lst):
  return str(int(round(sum(eval(e.replace('=','==')) for e in lst) / len(lst) * 100, 0))) + '%'

