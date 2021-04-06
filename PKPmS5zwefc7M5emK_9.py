
def missing_angle(angle1, angle2):
  if 180 - (angle1 + angle2) == 90:
    return 'right'
  if 180 - (angle1 + angle2) > 90:
    return 'obtuse'
  if 180 - (angle1 + angle2) < 90:
    return 'acute'

