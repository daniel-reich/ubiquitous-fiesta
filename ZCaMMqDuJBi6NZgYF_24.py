
def temp_conversion(celsius):
  f = celsius*9/5 +32
  k = celsius+ 273.15
  if k <0:
    return ("Invalid")
  list = []
  list.append(round(f,2))
  list.append(round(k,2))
  return list

