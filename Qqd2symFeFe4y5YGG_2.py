
def palindromic_date(date):
  dd,mm,yyyy = date.split('/')
  date1 = ''.join([dd,mm,yyyy])
  date2 = ''.join([mm,dd,yyyy])
  return date1 == date1[::-1] and date2 == date2[::-1]

