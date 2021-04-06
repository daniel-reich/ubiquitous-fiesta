
def get_type(value):
  if(type(value) == str): 
    return "str"
  if(type(value) == bool):
    return "bool"
  if(type(value) == int):
    return "int"
  if(type(value) == list):
    return "list"
  if(type(value) == set):
    return "set"
  if(type(value) == tuple):
    return "tuple"
  if(type(value) == dict):
    return "dict"
  else:
    return "NoneType"

