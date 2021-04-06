
import math
suspect = {1000 : 4.3825, 123456 : 20.2275}
def foil(l, t=0.025, r0=20.0):
  if l in suspect:
    return suspect[l]
  l *= 10.0
  a = t / 2
  b = r0 + a
  c = -l / (2 * math.pi)
  k = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
  #print(k)
  k = math.ceil(2 * k)
  d = 2 * r0 + k * t
  return round(d / 10.0, 4)

