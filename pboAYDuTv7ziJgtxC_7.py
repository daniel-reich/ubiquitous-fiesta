
def min_turns(current, target):
  res = 0
  for current_num, target_num in zip(current, target):
    diff = abs( int(current_num) - int(target_num) )
    res += diff if diff <= 5 else 10 - diff
  return res

