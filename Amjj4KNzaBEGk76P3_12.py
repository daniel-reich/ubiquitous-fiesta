
def chemical_reactions(carbon, hydrogen, oxygen):
    water = min(hydrogen // 2, oxygen)
    hydrogen -= water * 2
    oxygen -= water
    dioxide = min(carbon, oxygen // 2)
    carbon -= dioxide
    oxygen -= dioxide * 2
    methane = min(carbon, hydrogen // 4)
    return [water, dioxide, methane]

