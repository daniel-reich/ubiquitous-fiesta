
def data_type(value):
  t = type(value).__name__
  if t == 'dict':
    return 'dictionary'
  elif t == 'str':
    return 'string'
  elif t == 'int':
    return 'integer'
  else:
    return t

