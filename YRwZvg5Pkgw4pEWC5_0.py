
def flick_switch(lst):
  res, state = [], True
  for i in lst:
    if i == 'flick':
      state = not state
    res.append(state)
  return res

