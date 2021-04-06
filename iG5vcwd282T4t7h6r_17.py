
def str_to_dict(lst):
  dic={}
  for i in lst:
    a=i.split("=")
    dic[a[0]]=a[1]
  return dic

