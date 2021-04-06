
def chemical_reactions(carbon, hydrogen, oxygen):
  final = [0,0,0]
    #for h2o
  h2o = 0
  if hydrogen != 0 and oxygen != 0:
    while hydrogen > 1 and oxygen > 0:
      hydrogen -= 2
      oxygen -= 1
      h2o += 1
    final[0] = h2o
  else:
    final[0] = 0
​
    #for co2
  co2 = 0
  if carbon != 0 and oxygen != 0:
    while carbon > 0 and oxygen > 1:
      carbon -= 1
      oxygen -= 2
      co2 += 1
    final[1] = co2
  else:
    final[1] = 0
​
  #for ch4
  ch4 = 0
  if carbon != 0 and hydrogen != 0:
    while carbon > 0 and hydrogen > 3:
      carbon -= 1
      oxygen -= 4
      ch4 += 1
    final[2] = ch4
  else:
    final[2] = 0
​
  return final

