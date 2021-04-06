
from math import pi
def foil(length):
    diam=4
    cir=0
    while length>0:
        cir=pi*diam 
        length-=cir
        diam+=.0050
    return round(diam-.0025*(cir/2+length<0),4)

