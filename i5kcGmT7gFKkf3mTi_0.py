
def data_type(value):
  c=value.__class__.__name__
  return c+{'dict': 'ionary', 'str': 'ing', 'int': 'eger'}.get(c, '')

