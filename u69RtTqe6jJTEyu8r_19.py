
import math
​
def impedance_calculator(Dd, Dc, er):
    Z = 138.0 * math.log(Dd / Dc, 10) / math.sqrt(er)
    return round(Z, 1)

