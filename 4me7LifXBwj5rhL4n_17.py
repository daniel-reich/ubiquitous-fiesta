
import math
​
def circle_or_square(rad, area):
  perimetro_circulo = 2*3.14*rad
  perimetro_cuadrado =4 * math.sqrt(area) 
  if perimetro_circulo > perimetro_cuadrado:
    return True
  else: 
    return False

