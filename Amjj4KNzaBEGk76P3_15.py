
def chemical_reactions(carbon, hydrogen, oxygen):
    h2o = min(oxygen, hydrogen//2)
    hydrogen -= h2o*2
    oxygen -= h2o
    co2 = min(carbon, oxygen//2)
    carbon -= co2
    oxygen = co2*2
    ch4 = min(carbon, hydrogen//4)
    return [h2o, co2, ch4]

