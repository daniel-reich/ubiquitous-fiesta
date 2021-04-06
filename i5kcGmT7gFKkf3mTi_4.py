
def data_type(value):
  return {
    'str': 'string',
    'dict': 'dictionary',
    'bool': 'boolean',
    'list': 'list',
    'float': 'float',
    'int': 'integer',
    'date': 'date'
  }[value.__class__.__name__]

