
def face_interval(num):
  if type(num) != list:
    return ":/"
  elif (max(num) - min(num)) in num:
    return ":)"
  else:
    return ":("

