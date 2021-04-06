
def data_type(value):
  type_dict = {"list": "list", "dict": "dictionary", "str": "string", "int": "integer", "float": "float", "bool": "boolean", "date": "date"}
  return type_dict[str(type(value).__name__)]

