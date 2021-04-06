
def freed_prisoners(prison):
  if prison[0] == 0:
    return 0
  n = 1
  r = 0
  for x in prison:
    if x == n:
      n = (n + 1) % 2
      r += 1
  return r

