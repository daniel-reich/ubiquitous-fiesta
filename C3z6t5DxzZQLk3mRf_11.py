
def tune(lst):
  tun = [329.63, 246.94, 196.00, 146.83, 110.00, 82.41]
  
  tunezzz = [" - ", " - ", " - ", " - ", " - ", " - "]
  for i in range(len(lst)):
    if lst[i] == 0:
      continue
  
    if float(lst[i]) == tun[i]:
      tunezzz[i] = "OK"
    else:
      dif = abs((lst[i] - tun[i])) / lst[i]
      dif *= 100
      dif = round(dif)    
      
      if lst[i] < tun[i]:
        if dif == 0:
          tunezzz[i] = "OK"
        elif dif < 3:
          tunezzz[i] = ">+"
        elif dif >= 3:
          tunezzz[i] = ">>+"
          
      elif lst[i] > tun[i]:
        if dif == 0:
          tunezzz[i] = "OK"
        elif dif < 3:
          tunezzz[i] = "+<"
        elif dif >= 3:
          tunezzz[i] = "+<<"
        
  return tunezzz

