
import math
def logarithm(base, num):
  if type(base) == int and type(num) == int:
    try:
      return round(math.log(num, base))
    except:
      return "Invalid"

