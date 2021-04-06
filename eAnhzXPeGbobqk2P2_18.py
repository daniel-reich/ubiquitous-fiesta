
def century(year):
  if str(year)[-2:] == '00': 
    return "{}th century".format(str(year)[:2])
  elif year <2000:
    return "{}th century".format(int(str(year)[:2])+1)
  else:
    return "{}st century".format(int(str(year)[:2])+1)

