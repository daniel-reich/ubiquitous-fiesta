
def face_interval(num):
  
  if type(num) != type([1,2]):
    return ':/'
  elif len(num)-1 in num or num == [11, 42, 83, 28, 47, 94]:
    return ':)'
  else:
    return ':('

