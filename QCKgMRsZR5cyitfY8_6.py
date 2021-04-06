
def get_type(value):
  typ = str(type(value))
  typ = typ.split()
  return typ[-1].strip('>').strip("''")

