
import math
​
def impedance_calculator(Dd, Dc, er):
    return round((138/math.sqrt(er))*math.log10(Dd/Dc),1)

