
def big_sub(lst):
  max_sum = max_start = max_end = curr_sum = 0
  for curr_end, x in enumerate(lst):
    if curr_sum <= 0:
      curr_start, curr_sum = curr_end, x
    else:
      curr_sum += x
    if curr_sum >= max_sum:
      max_sum, max_start, max_end = curr_sum, curr_start, curr_end
  return [max_sum, max_start, max_end]

