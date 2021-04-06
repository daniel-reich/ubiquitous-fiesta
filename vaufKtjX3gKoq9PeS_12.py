
def ohms_law(v, r, i):
  if [v, r, i].count(None) != 1: return "Invalid"
  try:
    return round(r * i, 2)
  except:
    try:
      return round(v / i, 2)
    except:
      return round(v / r, 2)

