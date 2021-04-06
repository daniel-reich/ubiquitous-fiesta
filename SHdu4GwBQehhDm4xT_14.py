
def freed_prisoners(prison):
  if prison[0] == 0:
    return 0
  i = 0
  c = 0
  while i < len(prison):
    if prison[i] == 1:
      c += 1
      for j in range(len(prison)):
        if prison[j] == 1:
          prison[j] = 0
        else:
          prison[j] = 1
    i += 1
  return c

