
def match_houses(step):
  if step == 0:
    return 0
  count = 6
  next = 5
  for i in range(1, step):
    count += next
  return count

