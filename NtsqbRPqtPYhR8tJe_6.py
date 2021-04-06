
def blocks(step):
  if step == 0: return 0
  sum = 5
  increase_by = 6
  for i in range(0, step-1):
    increase_by = increase_by + 1
    sum = sum + increase_by
  return sum

