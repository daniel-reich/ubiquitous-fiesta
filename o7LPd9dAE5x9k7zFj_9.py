
def logarithm(base, num):
  from math import log
  try:  
    return int(log(num) / log(base))
  except:
    return 'Invalid'

