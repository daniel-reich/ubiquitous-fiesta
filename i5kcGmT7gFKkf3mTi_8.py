
def data_type(value):
  if type(value) == list:
    return 'list'
  elif type(value) == dict:
    return 'dictionary'
  elif type(value) == str:
    return 'string'
  elif type(value) == int:
    return 'integer'
  elif type(value) == float:
    return 'float'
  else:
    return 'date'

