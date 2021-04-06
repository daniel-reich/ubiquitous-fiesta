
def str_to_dict(l):
  d={}
  for i in l:t=i.split('=');d[t[0]] = t[1]
  return d

