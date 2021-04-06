
def palindromic_date(date):
  dd, mm, yy = date.split('/')
  ddmm = dd + mm + yy
  mmdd = mm + dd + yy
  
  date_rev1 = ddmm[::-1]
  date_rev2 = mmdd[::-1]
  
  date = date.replace('/', '')
  
  if date == date_rev1 and date == date_rev2: return True
  else: return False

