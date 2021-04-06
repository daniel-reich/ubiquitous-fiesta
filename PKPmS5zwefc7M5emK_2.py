
def missing_angle(angle1, angle2):
  angle3 = 180 - (angle1 + angle2)
  return "right" if angle3 == 90 else "obtuse" if angle3>90 else "acute"

