
from math import log
def impedance_calculator(Dd,Dc,er):
    return round(59.93 * log(Dd / Dc) / pow(er, 0.5), 1)

