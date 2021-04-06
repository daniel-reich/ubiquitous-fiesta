
def power_morphic(num):
  powlst = []
  for i in range(2,10):
    powlst.append(num**i)
  print(powlst)
  powcnt = 0
  for p in powlst:
    p = str(p)
    n = str(num)
    print(p[(len(p)-len(n)):len(p)])
    print(n)
    if p[(len(p)-len(n)):len(p)] == n:
      powcnt+=1
  if powcnt==8:
    return "Polymorphic"
  elif powcnt == 4:
    return 'Quadrimorphic'
  elif powcnt == 2:
    return 'Dimorphic'
  elif powcnt == 1:
    return 'Enamorphic'
  else:
    return 'Amorphic'

