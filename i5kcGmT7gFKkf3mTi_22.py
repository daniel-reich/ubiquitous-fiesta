
def data_type(value):
  if isinstance(value, dict):
      return "dictionary"
  elif isinstance(value, str):
      return "string"
  elif isinstance(value, int):
      return "integer"
  else:
      return type(value).__name__

