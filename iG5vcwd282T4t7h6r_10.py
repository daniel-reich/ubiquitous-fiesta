
def str_to_dict(lst):
  dict={}
  for i in range(len(lst)):
    dict.__setitem__(lst[i].split("=")[0],lst[i].split("=")[1])
  return dict

