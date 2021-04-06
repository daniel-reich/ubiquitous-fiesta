
def get_type(value):
  type3 = str(type(value))
  type2 = ''
  isType = False
  for y in type3:
    if(y == '\'' and isType):
      break
    if(isType):
      type2 += y
    if(y == '\'' and not isType):
      isType = True
  return type2

