
def chemical_reactions(carbon, hydrogen, oxygen):
  H2O = 0 
  CO2 = 0 
  CH4 = 0 
  if hydrogen >= 2*oxygen: 
    H2O = oxygen
  else:
    H2O = hydrogen//2
  if oxygen-H2O >= 2*carbon: 
    CO2 = carbon
  else:
    CO2 = (oxygen-H2O)//2
  if hydrogen-2*H2O >= 4*(carbon-CO2):
    CH4 = carbon-CO2
  else:
    CH4 = (hydrogen-2*H2O)//4
  molecules = [H2O, CO2, CH4] 
  return molecules

