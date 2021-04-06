
def list_values_types(lst):
  n = []
  for i in lst:
    if type(i) == int:
      n.append('int')
    elif type(i) == str:
      n.append('str')
    elif type(i) == list:
      n.append('list')
    elif type(i) == bool:
      n.append('bool')
    elif type(i) == []:
      print(type(i))
      n.append('NoneType')
    elif type(i) == float:
      n.append('float')
    elif type(i) == dict:
      n.append('dict')
    else:
      print(type(i))
      n.append('NoneType')
  return n

