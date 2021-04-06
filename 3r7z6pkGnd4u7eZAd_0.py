
def mark_maths(lst):
  return '{:.0%}'.format(sum(eval(i.replace('=', '==')) for i in lst)/len(lst))

