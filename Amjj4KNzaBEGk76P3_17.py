
def chemical_reactions(carbon, hydrogen, oxygen):
  ## assign temp variables
  temp_hydrogen = hydrogen
  temp_oxygen = oxygen
  temp_carbon = carbon
  total_h20 = 0
  total_c02 = 0
  total_ch4 = 0
  while temp_hydrogen >= 2 and temp_oxygen >= 1:
    temp_hydrogen -= 2
    temp_oxygen -= 1
    total_h20 += 1
  while temp_carbon >= 1 and temp_oxygen >= 2:
    temp_oxygen -= 2
    temp_carbon -= 1
    total_c02 += 1
  while temp_carbon >= 1 and temp_hydrogen >= 4:
    temp_carbon -= 1
    temp_hydrogen -= 4
    total_ch4 += 1
  return [total_h20,total_c02,total_ch4]

