
def back_to_home(directions):
  countN = 0
  countS = 0
  countE = 0
  countW = 0
  for let in directions:
        if let == 'N':
            countN = countN + 1
        if let == 'S':
            countS = countS + 1
        if let == 'E':
            countE = countE + 1            
        if let == 'W':
            countW = countW + 1
  if countN == countS and countE == countW:
        return True
  else:
        return False

