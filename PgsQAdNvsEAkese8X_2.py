
def to_list(dct):
  list = []
  for key,value in dct.items():
    list.append([key,value])
  list.sort()
  return list

