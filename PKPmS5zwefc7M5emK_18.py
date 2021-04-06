
def missing_angle(angle1, angle2):
  sum=angle1+angle2
  rem=180-sum
  if rem>90 and rem<180:
    return "obtuse"
  elif rem==90:
    return "right"
  else:
    return "acute"
missing_angle(27, 59)

