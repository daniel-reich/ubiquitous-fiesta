
def mark_maths(lst):
  correct = sum(eval(i.replace('=', '==')) for i in lst)
  return '{:.0%}'.format(correct / len(lst))

