
def missing_angle(angle1, angle2):
  angle_remainder = 180 - (angle1 + angle2)
  if angle_remainder < 90:
    return "acute"
  elif angle_remainder == 90:
    return "right"
  else:
    return "obtuse"

