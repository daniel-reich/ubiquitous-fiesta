
def flick_switch(lst):
  toggle = True
  result = []
  for word in lst:
    if (word != 'flick'):
      result.append(toggle)
    elif (word == 'flick'):
      toggle = not toggle
      result.append(toggle)
    
  return result

