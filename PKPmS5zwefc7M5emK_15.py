
def missing_angle(angle1, angle2):
  if 180 > (angle1 + angle2) > 90:
    return "acute"
  if (angle1 + angle2) == 90:
    return "right"
  if 90> (angle1 + angle2) > 0:
    return "obtuse"

