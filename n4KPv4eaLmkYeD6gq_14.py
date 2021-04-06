
def face_interval(num):
  if type(num)!=list:
    return ':/'
  return ':)' if (max(num)-min(num)) in num else ':('

