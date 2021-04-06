
def chemical_reactions(C,H,O):
  greater = max(H//2,O)
  if greater == H//2:
    H2O = O
    c_H = H-O*2
    c_O = 0
  else:
    H2O = H//2
    c_H = 0
    c_O = O - H//2
  grea = max(c_O//2,C)
  if grea == c_O//2:
    CO2 = C
    c_C = 0
  else:
    CO2 = c_O//2
    c_C = C - c_O//2
  gre = max(c_H//4,c_C)
  if gre == c_H//4:
    CH4 = c_C
  else:
    CH4 = c_H//4
  return list((H2O,CO2,CH4))

