
def flick_switch(lst):
  res = []
  sign = True
  for i in lst:
    if i  != 'flick':
      res.append(sign)
    else:
      sign = not sign
      res.append(sign)
      
  return res

