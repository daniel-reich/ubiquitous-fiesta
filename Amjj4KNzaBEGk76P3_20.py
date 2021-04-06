
def chemical_reactions(c, h, o):
  h2o = min(h // 2, o)
  co2 = min(c, (o - h2o) // 2)
  ch4 = min(c - co2, (h - h2o * 2) // 4)
  return [h2o, co2, ch4]

