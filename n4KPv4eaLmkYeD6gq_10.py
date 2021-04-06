
def face_interval(num):
  if isinstance(num,list):
    return ':)' if max(num)-min(num) in num else ':('
  return ':/'

