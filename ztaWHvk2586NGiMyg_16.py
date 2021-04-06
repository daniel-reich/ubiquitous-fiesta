
def is_truthy(val):
  if val is False:
    return 0
  elif val == None:
    return 0
  elif val == 0:
    return 0
  elif val == '':
    return 0
  elif val == []:
    return 0
  elif val == {}:
    return 0
  else:
    return 1

