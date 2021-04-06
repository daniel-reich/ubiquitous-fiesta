
def data_type(value):
  return  {int: 'integer', list: 'list', str: 'string', dict: 'dictionary', set: 'set', tuple: 'tuple', float:'float', datetime.date: 'date'}.get(type(value))

