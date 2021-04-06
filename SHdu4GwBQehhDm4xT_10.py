
def freed_prisoners(prison):
  freed_prisoners = 0
  if prison[0] == 0:
    return freed_prisoners
  for i in range(len(prison)):
    if prison[i] == 1:
      freed_prisoners += 1
      prison = [1 - cell for cell in prison]
  return freed_prisoners

