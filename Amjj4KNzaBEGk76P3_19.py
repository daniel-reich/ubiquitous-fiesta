
def chemical_reactions(carbon, hydrogen, oxygen):
  water = min(hydrogen//2,oxygen)
  hydrogen,oxygen = hydrogen-water*2,oxygen-water
  carbon_dioxide = min(carbon,oxygen//2)
  carbon,oxygen = carbon-carbon_dioxide,oxygen-carbon_dioxide*2
  methane = min(carbon,hydrogen//4)
  return [water,carbon_dioxide,methane]

