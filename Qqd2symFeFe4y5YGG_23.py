
def palindromic_date(date):
  a,b,c=date.split("/")
  return a[::-1]+b[::-1]==c

