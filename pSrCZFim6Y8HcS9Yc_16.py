
def convert(deg): 
  try:
    val,unit=deg.split('*')
    val=float(val)
  except ValueError:
    return 'Error'
  if unit=='C':
    return ('%d' % int(round((9*val)/5+32)))+ '*F'
  elif unit=='F':
    return ('%d' % int(round((5*(val-32))/9)))+ '*C'
  else: return 'Error'

