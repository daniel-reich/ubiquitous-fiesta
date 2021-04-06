
def divide(x, y):
  if abs(x) < abs(y):
    return 0
  elif x < 0 and y < 0:
    return 1 + divide(abs(x)-abs(y),abs(y))
  elif x < 0:
    return -1 - divide(abs(x+y),y)
  elif y < 0:
    return -1 - divide(x-abs(y),abs(y))
  else:
    return 1 + divide(x-y,y)

