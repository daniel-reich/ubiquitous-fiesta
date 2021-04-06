
def missing_angle(angle1, angle2):
  sum_angles = angle1 + angle2
  missing = 180 - sum_angles
  if missing == 90:
    return("right")
  if missing < 90:
    return("acute")
  if missing > 90:
    return("obtuse")

