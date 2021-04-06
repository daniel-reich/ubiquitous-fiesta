
def freed_prisoners(prison):
  counter = 0
  if(prison[0] == 0):
    return 0
  for cell in prison:
    if(cell == 1):
      counter += 1
      for num in range(0, len(prison)):
        if(prison[num] == 0):
          prison[num] = 1
        elif(prison[num] == 1):
          prison[num] = 0
  return counter

