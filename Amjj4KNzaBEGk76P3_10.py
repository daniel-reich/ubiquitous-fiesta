
def chemical_reactions(c, h, o):
    H2O = min(o, h//2)
    CO2 = min(c, ((o - H2O)//2))
    CH4 = min((c-CO2),(h-2*H2O)//4)
    return [H2O,CO2,CH4]

