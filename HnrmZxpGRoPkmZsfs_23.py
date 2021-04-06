
def is_valid_date(d, m, y):
  if not 0<m<13 or not 0<d<32: #false case
    return False
  elif m==2: #february
    return d<29 or (d==29 and y%4==0)
  else:#rest
    return d<31 or (d==31 and m in [1,3,5,7,8,10,12])

