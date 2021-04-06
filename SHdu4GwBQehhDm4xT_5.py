
def freed_prisoners(prison):
  pos = 0
  count = 0
  length = len(prison)
  if prison[0] != 1:
    return 0
  while pos < length:
    for i in range(pos, length):
      if prison[i] == 1:
        prison = [1 - x for x in prison]
        pos = i + 1
        count = count + 1
        break
      else:
        pos = i + 1
  return count

