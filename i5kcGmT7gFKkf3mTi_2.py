
import datetime
​
TYPE_NAMES_MAP = {
  list: 'list',
  dict: 'dictionary',
  str: 'string',
  int: 'integer',
  float: 'float',
  datetime.date: 'date',
}
​
def data_type(value):
  return TYPE_NAMES_MAP.get(type(value))

