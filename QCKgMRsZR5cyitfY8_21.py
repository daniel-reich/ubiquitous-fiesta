
def get_type(value):
  ty = str(type(value))
  ty = ty.replace("<class '","")
  ty = ty.replace("'>","")
  return ty

