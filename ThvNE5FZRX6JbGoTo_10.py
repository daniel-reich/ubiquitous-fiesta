
def inverter(txt, t):
  L=txt.split()
  if t=='P':
    return ' '.join(L[::-1]).capitalize()
  else:
    A=[x[::-1] for x in L]
    return ' '.join(A).capitalize()

