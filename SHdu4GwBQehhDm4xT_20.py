
def freed_prisoners(prison):
  cnt, i = 0, 0
  if prison[0] == 0:
    return 0
  while i < len(prison):
    if prison[i] == 1:
      cnt += 1
      prison = [int(not bool(x)) for x in prison[i + 1:]]
      i = 0
    else:
      i += 1
  return cnt

