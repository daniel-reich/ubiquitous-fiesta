
def chemical_reactions(carbon, hydrogen, oxygen):
  water = min(hydrogen // 2, oxygen)
  hydrogen -= 2 * water
  oxygen -= water
  carbon_dioxide = min(carbon, oxygen // 2)
  carbon -= carbon_dioxide
  oxygen -= carbon_dioxide
  return [
    water,
    carbon_dioxide,
    min(carbon, hydrogen // 4)
  ]

