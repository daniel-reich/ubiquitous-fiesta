
def tune(lst):
  tuning = {1:329.63,2:246.94,3:196.00,4:146.83,5:110.00,6:82.41}
​
  for i in range(len(lst)):
    if lst[i] == 0:
      lst[i] = ' - '
    else:
      diff = round(((lst[i]/tuning[i+1])-1)*100)
      if abs(diff) > 2:
        lst[i] = '+<<' if diff > 0 else '>>+'
      elif 2 >= abs(diff) > 0:
        lst[i] = '+<' if diff > 0 else '>+'
      else:
        lst[i] = 'OK'
  return lst

