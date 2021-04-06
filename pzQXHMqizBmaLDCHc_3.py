
def calculate_damage(a, b, x, y):
  
  effectiveness = 1
  
  if (a == "fire" and b == "water") or (a == "water" and b == "grass") or (a == "water" and b == "electric") or (a == "grass" and b == "fire"):
    effectiveness *= 0.5
  elif (a == "fire" and b == "electric") or (a == "grass" and b == "electric") or (a == "electric" and b == "fire") or (a == "electric" and b == "grass"):
    pass
  else:
    effectiveness *= 2
  
  return 50 * (x / y) * effectiveness

