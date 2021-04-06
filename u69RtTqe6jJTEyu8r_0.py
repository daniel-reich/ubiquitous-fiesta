
from math import sqrt , log10
def impedance_calculator(Dd,Dc,er):
    Zo=(138*log10(Dd/Dc))/sqrt(er)
    return round(Zo,1)

