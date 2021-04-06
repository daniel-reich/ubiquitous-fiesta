
def convert(deg):
  try:
    d, t = deg.split('*')
  except ValueError:
    return 'Error'
  if t == 'C': 
    return '{:.0f}*F'.format(int(d) * 1.8 + 32)
  elif t =='F':
    return '{:.0f}*C'.format((int(d) -32) / 1.8 )

