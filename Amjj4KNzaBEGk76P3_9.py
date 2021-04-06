
def chemical_reactions(carbon, hydrogen, oxygen):
  C = carbon  #new variables to edit current elements later
  H = hydrogen
  O = oxygen
  H2O = min(H // 2, O)  # // because only whole number reactions
  H -= H2O * 2
  O -= H2O
  CO2 = min(C, O // 2)
  C -= CO2
  O -= CO2 * 2
  CH4 = min(C, H // 4)
  C -= CH4
  O -= CH4 * 4
  return [H2O, CO2, CH4]

