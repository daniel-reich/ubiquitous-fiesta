
def palindromic_date(date):
  d,m,y = date.split("/")
  return d+m+y == (d+m+y)[::-1] and m+d+y == (m+d+y)[::-1]

