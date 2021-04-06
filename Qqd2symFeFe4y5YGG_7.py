
def palindromic_date(date):
  d = date.split("/")
  dmy = "".join(d)
  mdy = d[1] + d[0] + d[2]
  return dmy == dmy[::-1] and mdy == mdy[::-1]

