
def can_see_stage(seats):
  s = [list(t) for t in zip(*seats[::-1])]
  for j in s:
    for i in range(1, len(j)):
      if j[i-1] <= j[i]:
        return False
  return True

