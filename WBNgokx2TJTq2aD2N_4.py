
def smallest(digits, value):
  times_factor = 1
  original_value = value
  while len(str(value))!=digits:
    value= original_value*times_factor
    times_factor+=1
    
  return value

