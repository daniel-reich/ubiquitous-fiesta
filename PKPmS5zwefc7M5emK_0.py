
def missing_angle(angle1, angle2):
  if (angle1+angle2) < 90: return "obtuse"
  if (angle1+angle2) == 90: return "right"
  if (angle1+angle2) > 90: return "acute"

