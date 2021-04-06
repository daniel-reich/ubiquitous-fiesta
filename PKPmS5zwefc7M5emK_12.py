
def missing_angle(angle1, angle2):
  angle_name = ['acute','right','obtuse']
  total_angle = 180
  if total_angle - angle1 - angle2 < 90:
    return angle_name[0]
  elif total_angle -angle1 - angle2 == 90:
    return angle_name[1]
  else:
    return angle_name[-1]

