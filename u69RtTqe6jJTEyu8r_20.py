
import math
def impedance_calculator(Dd, Dc, er):
    return round(138*math.log10(Dd/Dc) / math.sqrt(er), 1)

