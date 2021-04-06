
def bird_code(lst):
  no_hyphens = list(' '.join(x.split('-')) for x in lst)
  res = []
  for x in no_hyphens:
    txt = x.split()
    if len(txt)==1:
      res.append(txt[0][0:4].upper())
    elif len(txt)==2:
      res.append(txt[0][0:2].upper()+txt[1][0:2].upper())
    elif len(txt)==3:
      res.append(txt[0][0].upper()+txt[1][0].upper()+txt[2][0:2].upper())
    else:
      res.append(txt[0][0].upper()+txt[1][0].upper()+txt[2][0].upper()+txt[3][0].upper())
  return res

