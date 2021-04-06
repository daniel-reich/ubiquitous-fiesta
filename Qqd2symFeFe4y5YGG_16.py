
def palindromic_date(date):
  a = ''.join(date.split('/'))
  b = a[2:4] + a[0:2] + a[4:]
  if a == a[::-1] and a[::-1] == b:
    return True
  else:
    return False

