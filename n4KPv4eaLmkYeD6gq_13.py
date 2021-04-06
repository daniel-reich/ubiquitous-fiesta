
def face_interval(num):
  strtest = ''
  if (type(num) == list):
    gap=max(num) - min(num)
    if(gap in num):
      strtest += ':)'
    else:
      strtest += ':('
  else:
    strtest += ':/'
  return strtest

