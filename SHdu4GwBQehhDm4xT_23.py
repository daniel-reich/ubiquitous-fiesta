
def freed_prisoners(prison):
  prison = list(enumerate(prison))
  newPrison = []
  
  if prison[0][1] == 0:
    return 0
  
  for cell in prison:
    if cell[0] != len(prison)-1:
      if cell[1] == 1 and prison[cell[0]+1][1] == 0:
        newPrison.append(cell[1])
      elif cell[1] == 0 and prison[cell[0]+1][1] == 1:
        newPrison.append(cell[1])
    elif cell[0] == len(prison)-1 and cell[1] != prison[::-1][1]:
      newPrison.append(cell[1])
      
  return len(newPrison)

