
def palindromic_date(date):
  d,m,y = date.split('/')
  return d==m and d+m==y[::-1]

