
def clean_up(files, sort):
  res = []
  for f in files:
    name, ext = f.split('.')
    group = [i for i in files if (i.startswith(name) if sort == 'prefix' else i.endswith(ext))]
    if group not in res:
      res.append(group)
  return res

