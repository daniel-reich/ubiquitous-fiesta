
def data_type(value):
  if type(value) is list:
    return 'list'
  if type(value) is dict:
    return 'dictionary'
  if type(value) is str:
    return 'string'
  if type(value) is int:
    return 'integer'
  if type(value) is float:
    return 'float'
  if type(value) is bool:
    return 'boolean'
  if type(value) is datetime.date:
    return 'date'

