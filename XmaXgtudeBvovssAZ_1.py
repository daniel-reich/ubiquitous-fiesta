
from math import pi,sin,atan
def red_area(r):
    ang=pi-2*atan(.5)
    return round(r*r*pi/4-r*r*(ang-sin(ang))/2,3)

