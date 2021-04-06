
def list_values_types(lst):
  return [str(type(i)).replace('<class ','').replace('>','').replace("'",'') for i in lst]

