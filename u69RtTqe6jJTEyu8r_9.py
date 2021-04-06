
import math
def impedance_calculator(Dd, Dc, er):
    return round((138 / (er ** 0.5)) * math.log10(Dd/Dc),1)

