
def count_datatypes(*args):
  d=[int, str, bool, list, tuple, dict]
  v=[0,0,0,0,0,0]
  for i in range(len(args)):
    for j in range(len(d)):
      if type(args[i])==d[j]:
        v[j]=v[j]+1
  return v

