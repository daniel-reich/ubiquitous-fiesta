
def convert(deg):
  split_deg = deg.split('*')
  
  if len(split_deg) == 1:
    return 'Error'
  else:
    degree = int(split_deg[0])
    unit = split_deg[1]
    converted_unit = 'F'
    if unit == 'C':
      degree = degree * 9 / 5 + 32; 
    else:
      converted_unit = 'C'
      degree = (degree - 32) * 5 / 9
  return str(round(degree)) + '*' + converted_unit

