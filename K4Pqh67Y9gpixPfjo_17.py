
def is_valid_PIN(pin):
  if str(pin).isdigit() :
    if len(str(pin)) == 4 or len(str(pin)) == 6 :
      return True
    else : 
      return False
  else : 
    return False

