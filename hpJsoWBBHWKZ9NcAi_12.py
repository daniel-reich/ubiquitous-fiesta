
def bird_code(lst):
  outlst = []
  for x in lst:
      x = x.replace('-',' ')
      x = x.split()
      if len(x) == 1:
          outlst.append(x[0][:4].upper())
      elif len(x) == 2:
          outlst.append(x[0][:2].upper() + x[1][:2].upper())
      elif len(x) == 3:
          outlst.append(x[0][:1].upper() + x[1][:1].upper() + x[2][:2].upper())
      elif len(x) == 4:
          outlst.append(x[0][:1].upper() + x[1][:1].upper() + x[2][:1].upper() + x[3][:1].upper())
  return outlst

