
def str_to_dict(lst):
  dic = {}
  for x in lst:
    t = x.split("=")
    dic[t[0]] = t[1]
  return dic

