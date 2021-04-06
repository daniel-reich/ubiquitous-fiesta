
def is_valid_PIN(pin):
  arr=pin.split()
  z=0
  if len(pin)==0:
    return False
  if arr[0].isnumeric()==True:
    z=1
  if len(pin)==4 or len(pin)==6:
    if z==0:
      return False
    return True
  else:
  
    return False

