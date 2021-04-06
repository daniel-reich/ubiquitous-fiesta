
def freed_prisoners(prison):
  count = 0
  if prison[0] == 0:
    return 0
  for i in range(len(prison)):
    if prison[i] == 1:
      prison = [0 if prison[i] == 1 else 1 for i in range(len(prison))]
      count+=1
  return count

