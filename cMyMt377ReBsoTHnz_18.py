
def dict_to_list(d):
  ke = []
  re = []
  for key in d.keys():
    ke.append(key)
  ke.sort()
  for i in ke:
    re.append((i,d[i]))
  return re

