
def freed_prisoners(prison):
  freed_prisoners = 0
  isswapped = False
  if prison[0] == 0:
    return 0
  
  for cell in prison:
    if cell == 1 and isswapped == False:
      freed_prisoners += 1
      isswapped = True
    elif cell == 0 and isswapped == True:
      freed_prisoners += 1
      isswapped = False
      
  return freed_prisoners

