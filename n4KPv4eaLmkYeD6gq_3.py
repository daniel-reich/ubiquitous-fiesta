
def face_interval(num):
  if type(num)!=list:
    return ':/'
  return ':)' if num[-1]-num[0] in num else ':('

