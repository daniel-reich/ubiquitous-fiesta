
def tower_hanoi(discs):
  if discs ==0:
    return 0
  else:
    lista = []
    x = 7
    for i in range(discs-2):
      lista.append(x)
      x = x*2+1
    return lista[-1]

