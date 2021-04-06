
import math
def hit_prince(vo, th, yo, ds):
  vxo = vo * math.cos(th*3.14/180)
  vyo = vo * math.sin(th*3.14/180)
  g=9.81
  trise = vyo/g 
  h=yo + vyo*trise - 0.5*g*trise**2
  tfall=  (2*h/g)**(0.5)
  r=(trise+tfall)*vxo
  return abs(r-ds)<0.5

