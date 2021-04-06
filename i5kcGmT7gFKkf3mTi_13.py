
import datetime
​
def data_type(value):
  print(value, type(value))
  if type(value) == str:
    return "string"
  elif type(value) == dict:
    return "dictionary"
  elif type(value) == list:
    return "list"
  elif type(value) == int:
    return "integer"
  elif type(value) == float:
    return "float"
  elif type(value) == datetime.date:
    return "date"
  else:
    return None

