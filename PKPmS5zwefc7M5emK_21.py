
def missing_angle(angle1, angle2):
  third = 180 - angle1 - angle2
  if third == 90:
    return 'right'
  elif third > 90:
    return 'obtuse'
  return 'acute'

