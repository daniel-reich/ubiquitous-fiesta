
def missing_angle(angle1, angle2):
  if (180-angle1-angle2)<90:
    return 'acute'
  elif (180-angle1-angle2)==90:
    return 'right'
  elif 180>(180-angle1-angle2)>90:
    return 'obtuse'

