
def scale_tip(lst):
  left = sum([i for i in lst[:lst.index('I')]])
  right = sum([i for i in lst[lst.index('I')+1:]])
  if left > right:return 'left'
  elif right>left :return 'right'
  return 'balanced'

