
def chemical_reactions(carbon, hydrogen, oxygen):
  H2O = 0
  CO2 = 0
  CH4 = 0
  while hydrogen > 1 and oxygen > 0:
    H2O += 1
    hydrogen -= 2
    oxygen -= 1
  while oxygen > 1 and carbon > 0:
    CO2 += 1
    oxygen -= 2
    carbon -= 1
  while hydrogen > 3 and carbon > 0:
    CH4 += 1
    hydrogen -= 4
    carbon -= 1
  return [H2O, CO2, CH4]

