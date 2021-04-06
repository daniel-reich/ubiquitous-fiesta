
def happy_year(year):
  while 1:
    year+=1
    if len(set(str(year))) == 4:
      return year

