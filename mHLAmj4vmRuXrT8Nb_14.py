
def consecutive_combo(lst1, lst2):
  combi = sorted(lst1 + lst2)
  startnum = combi[0]
  for i in range(len(combi)):
    if(combi[i]!=startnum):
      return False
      break
    startnum += 1
    
  return True

