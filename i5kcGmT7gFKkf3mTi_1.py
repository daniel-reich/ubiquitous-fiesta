
def data_type(value):
  return {
    'int': 'integer',
    'list': 'list',
    'dict': 'dictionary',
    'str': 'string',
    'float': 'float',
    'bool': 'boolean',
    'datetime.date': 'date'
  }[str(type(value))[8:-2]]

