
def missing_angle(angle1, angle2):
  miss = 180 - angle1 - angle2
  if miss < 90:
    return "acute"
  elif miss == 90:
    return "right"
  else:
    return "obtuse"

