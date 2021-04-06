
def missing_angle(angle1, angle2):
  sum = angle1 + angle2
  if(sum > 90):
    return "acute"
  elif(sum < 90):
    return "obtuse"
  else:
    return "right"

