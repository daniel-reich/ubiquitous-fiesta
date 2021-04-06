
def chemical_reactions(carbon, hydrogen, oxygen):
  h2o=min(oxygen,hydrogen//2)
  co2=min(carbon,(oxygen-h2o)//2)
  ch4=min(hydrogen//4,carbon-co2)
  return [h2o,co2,ch4]

