
def data_type(value):
  s = str(type(value))[8:-2]
  if s=="dict": return "dictionary"
  if s == "str": return "string"
  if s=="int": return "integer"
  if s == "datetime.date": return "date"
  return s

