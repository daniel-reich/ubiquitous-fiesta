
def ohms_law(v, r, i):
  # V = R * I
  temp_list = [v, r, i]
  if temp_list.count(None) >= 2 or temp_list.count(None) == 0:
    result = "Invalid"
  elif v is None:
    result = round(r * i, 2)
  elif i is None:
    result = round(v / r, 2)
  else:
    result = round(v / i, 2)
  return result

