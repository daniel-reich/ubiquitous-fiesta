
def data_type(value):
  lookup = {
    'list':'list',
    'dict':'dictionary',
    'str':'string',
    'int':'integer',
    'float':'float',
    'date':'date',
    'boolean':'boolean'
  }
  return lookup[type(value).__name__]

