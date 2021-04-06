
def flick_switch(lst):
  result = []
  flag = True
  for i in lst:
    if i == 'flick':
      if flag == True:
        flag = False
      else:
        flag = True
    result.append(flag)
  return result

