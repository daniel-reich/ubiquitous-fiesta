
def scale_tip(lst):
  middle = len(lst)//2
  left_sum = 0
  right_sum = 0
  for x in range(middle):
    left_sum += lst[x]
  for y in range(middle):
    right_sum += lst[-y-1]
  if left_sum == right_sum:
    return "balanced"
  if left_sum >= right_sum:
    return "left"
  else:
    return "right"

