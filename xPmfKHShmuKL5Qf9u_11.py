
def scale_tip(lst):
  ind = 0
  for i in lst:
    if type(i) == str:
      ind = lst.index(i)
      break
  left = sum(lst[:ind])
  right = sum(lst[-ind:])
  if left > right:
    return 'left'
  elif left == right:
    return 'balanced'
  else:
    return 'right'

