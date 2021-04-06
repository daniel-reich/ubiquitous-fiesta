
def scale_tip(lst):
  i_index = lst.index("I")
  sum_left = sum(i for i in lst[:i_index])
  sum_right = sum(i for i in lst[i_index + 1:]) 
  if sum_left == sum_right:
    return "balanced"
  elif sum_left > sum_right:
    return "left"
  return "right"

