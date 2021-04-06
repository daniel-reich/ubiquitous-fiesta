
def scale_tip(lst):
  left, right = sum(lst[:lst.index('I')]), sum(lst[lst.index('I') + 1:])
  if left > right:
    return 'left'
  elif left < right:
    return 'right'
  else:
    return 'balanced'

