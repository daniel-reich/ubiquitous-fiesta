
def temp_conversion(celsius):
  lst = []
  lst.append(round(celsius*9/5 +32, 2))
  lst.append(round(celsius + 273.15, 2))
  if lst[1] <= 0:
    return "Invalid"
  return lst

