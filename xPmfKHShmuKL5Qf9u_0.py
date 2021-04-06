
def scale_tip(lst):
  v = lst.index('I')
  left, right = sum(lst[:v]), sum(lst[v+1:])
  return 'right' if right > left else 'left' if left > right else 'balanced'

