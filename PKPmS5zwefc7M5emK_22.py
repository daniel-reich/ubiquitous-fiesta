
def missing_angle(angle1, angle2):
  b=180-(angle1+angle2)
  if 90<b<180:
    return ("obtuse")
  elif (b==90):
    return ("right")
  elif (b<90):
    return ("acute")

