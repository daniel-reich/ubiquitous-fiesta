
def clear_ordering(lista):
  sup = {}
  for i in range(len(lista)):
    if lista[i][0] not in sup.keys():
      sup[lista[i][0]] = [lista[i][1]]
    else:
      sup[lista[i][0]].append(lista[i][1])
  print(sup)
  n = 0
  for valor in sup.values():
    if valor[0] not in list(sup.keys()):
      n += 1
      print(valor[0])
  
  if n != 1:
    return False
  else:
    return True

