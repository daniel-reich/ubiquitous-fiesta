
import math
def logarithm(base, num):
  try:
    if num % base != 0:
      return "Invalid"
    return math.log(num,base)
  except (ValueError, ZeroDivisionError):
    return "Invalid"

