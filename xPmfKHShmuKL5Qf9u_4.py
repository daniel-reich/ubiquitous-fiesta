
def scale_tip(lst):
  return "left" if sum(lst[:lst.index('I')]) > sum(lst[lst.index('I') + 1:]) else "right" if sum(lst[:lst.index('I')]) < sum(lst[lst.index('I') + 1:]) else 'balanced'

