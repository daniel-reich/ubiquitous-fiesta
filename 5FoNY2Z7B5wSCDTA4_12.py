
def happy_year(year):
  if len(set(str(year+1)))==4:return year+1
  return happy_year(year+1)

