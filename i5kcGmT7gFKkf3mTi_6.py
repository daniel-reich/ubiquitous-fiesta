
from datetime import date 
​
def data_type(value):
  value_type=type(value)
  types=["list","dictionary","string","integer","float","boolean","date"]
  if value_type == list:
    return types[0]
  elif value_type == dict:
    return types[1]
  elif value_type == str:
    return types[2]
  elif value_type == int:
    return types[3]
  elif value_type == float:
    return types[4]
  elif value_type == bool:
    return types[5]
  elif value_type == datetime.date:
    return types[6]

