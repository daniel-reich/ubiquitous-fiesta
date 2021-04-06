
def missing_angle(angle1, angle2):
  y = angle1 + angle2
  if y > 90:
    return "acute"
  elif y == 90:
    return "right"
  return "obtuse"

