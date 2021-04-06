
def clean_up(files, sort):
  res = []
  for x in files:
    x=x.split('.')
    tmp =[a for a in files if(a.startswith(x[0]) if sort=='prefix' else a.endswith(x[1]))]
    if tmp not in res:
      res.append(tmp)
  return res

