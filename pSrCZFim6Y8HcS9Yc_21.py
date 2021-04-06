
def convert(deg):
  if '*' not in deg or not deg[-1].isalpha():
    return 'Error'
  
  temp = int(deg[:-2])
  if 'C' in deg:
    temp = 9/5 * temp + 32
    return str(round(temp)) + '*F'
  else:
    temp = 5/9 * (temp - 32)
    return str(round(temp)) + '*C'

