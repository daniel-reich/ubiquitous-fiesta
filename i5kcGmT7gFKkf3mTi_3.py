
def data_type(value):
  types = {list: 'list', dict: 'dictionary', str: 'string', int: 'integer', 
           float: 'float', bool: 'boolean', datetime.date: 'date'}
       
  t = type(value)
  return types[t]

