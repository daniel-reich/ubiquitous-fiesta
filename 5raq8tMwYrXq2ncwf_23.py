
import re
def catch_zero_division(expr):
  try:
    temp=eval(expr)
    return False
  except:
    return True

