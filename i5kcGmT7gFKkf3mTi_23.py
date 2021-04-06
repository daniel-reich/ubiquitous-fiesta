
def data_type(value):
  name = type(value).__name__
  if name == 'dict':
    return 'dictionary'
  if name == 'str':
    return 'string'
  if name == 'int':
    return 'integer'
  return name

