
def will_fit(holds, cargo):
  
  for index, letter in enumerate(holds):
    if letter == 'S':
      if cargo[index] > 50:
        return False
        break
    
    if letter == 'M':
      if cargo[index] > 100:
        return False
        break
    
    if letter == 'L':
      if cargo[index] > 200:
         False
         break
         
  return True

