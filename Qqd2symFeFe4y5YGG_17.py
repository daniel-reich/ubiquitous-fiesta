
def palindromic_date(date):
  d, m, y = date.split('/')
  return ''.join([d,m,y])==''.join([d,m,y])[::-1] and ''.join([m,d,y])==''.join([m,d,y])[::-1]

