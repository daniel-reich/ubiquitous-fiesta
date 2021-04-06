
def flick_switch(lst):
  ans = []
  flag = True
  for i in lst:
    if i == 'flick':
      flag = not flag
    ans.append(True and flag)
  
  return ans

