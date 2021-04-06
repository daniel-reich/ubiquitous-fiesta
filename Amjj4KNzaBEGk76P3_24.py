
def chemical_reactions(carbon, hydrogen, oxygen):
    h2o = min(hydrogen // 2, oxygen)
    oxygen -= h2o
    hydrogen -= 2 * h2o
    co2 = min(carbon, oxygen // 2)
    oxygen -= 2 * co2
    carbon -= co2
    ch4 = min(carbon, hydrogen // 4)
    return [h2o, co2, ch4]

