
def is_repdigit(num):
  res = False
  num = str(num)
  for ch in num:
    if ch == num[0]:
      res = True
    else:
      res = False
      break
    
  return res

