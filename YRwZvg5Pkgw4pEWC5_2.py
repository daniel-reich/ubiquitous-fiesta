
def flick_switch(lst):
  flag = True
  switch_lst = []
  for elem in lst:
    if elem == 'flick':
      flag = not flag
      switch_lst.append(flag)
    else:
      switch_lst.append(flag)
  return switch_lst

