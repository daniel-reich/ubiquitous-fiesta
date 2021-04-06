
def is_rectangle(coordinates):
  cords=[eval(i) for i in coordinates]
  others=[]
  check=[]
  if len(cords)<4:
    return False
  for i in range(1,4):
    if cords[0][0] == cords[i][0]:
      others.append(cords[i])
    elif cords[0][1] == cords[i][1]:
      others.append(cords[i])
    else:
      check.append(cords[i])
  if len(check)!=1 or check[0][0] not in [others[0][0],others[1][0]] or check[0][1] not in [others[0][1],others[1][1]]:
    return False
  return True

