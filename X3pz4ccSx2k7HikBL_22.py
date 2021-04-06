
def showdown(p1, p2):
  time1 = 0
  time2 = 0
  for i in p1:
    if i != ' ':
      break
    else:
      time1+= 1
  
  for i in p2:
    if i != ' ':
      break
    else:
      time2+=1
  if time1 == time2:
    return ('tie')
  elif time1 < time2:
    return 'p1'
  else:
    return 'p2'

