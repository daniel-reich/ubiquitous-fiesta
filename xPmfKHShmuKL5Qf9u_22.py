
def scaleTip(lst):
  I_index = lst.index("I")
  if sum(lst[:I_index]) == sum(lst[I_index + 1:]):
    return "balanced"
  if sum(lst[:I_index]) > sum(lst[I_index + 1:]):
    return "left"
  if sum(lst[:I_index]) < sum(lst[I_index + 1:]):
    return "right"

