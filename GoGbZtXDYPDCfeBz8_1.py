
def magic(txt):
  month, day, year = [int(txt[:2]),int(txt[2:4]),txt[5:]]
  return True if year.endswith(str(month*day)) else False

