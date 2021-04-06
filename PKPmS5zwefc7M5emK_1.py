
def missing_angle(angle1, angle2):
  angle3 = 180 - angle1 - angle2
  if angle3 == 90:
    return "right"
  elif angle3 > 90:
    return "obtuse"
  else:
    return "acute"

