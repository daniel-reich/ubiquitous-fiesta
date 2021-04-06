
def palindromic_date(date):
  d, m, y = date.split('/')
  return d + m + y == m + d + y == date.replace('/','')[::-1]

