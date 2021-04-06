
def missing_angle(angle1, angle2):
  missing = 180 - (angle1 + angle2)
  if missing == 90:
    return "right"
  elif missing > 90:
    return "obtuse"
  elif missing < 90:
    return "acute"

