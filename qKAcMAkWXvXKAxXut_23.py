
def calc_bundled_temp(n, temp):
  split_string = temp.split("*")
  temp_outside = float(split_string[0])
  new_temp = round(((1.1)**n)*temp_outside,1)
  return str(new_temp) + "*C"
  #return str(((1.1)**n)*float(split_string[0]) + "*C"

