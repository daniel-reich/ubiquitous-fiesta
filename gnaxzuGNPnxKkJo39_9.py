
def easter_date(y):
  g = y%19 + 1
  s = (y - 1600) // 100 - (y - 1600)//400
  l = (((y - 1400) // 100) * 8)//25
  p_ = (3 - 11*g + s - l)%30
  if (p_ == 29) or (p_ == 28 and g > 11):
    p = p_ - 1
  else:
    p = p_
  d = (y + (y // 4) - (y // 100) + (y // 400))%7 
  d_ = (8 - d)%7
  pp=(3 + p)%7
  x_=d_ - pp
  x = (x_ - 1)%7 + 1
  e=p+x
  if e < 11:
    return 'March ' + str(int((e + 21)))
  else:
    return 'April ' + str(int(e - 10))

