
def missing_angle(one, two):
  if 180 - (one + two) < 90:
    return 'acute' 
  elif 180 - (one + two) > 90:
    return 'obtuse' 
  else: 
    return 'right'

