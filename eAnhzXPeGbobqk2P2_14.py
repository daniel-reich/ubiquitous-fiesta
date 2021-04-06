
def century(year):
  if year % 100 >= 1 and year % 100 <= 99 and int(str(year)[:2]) != 20:
    return ('{}th century').format(int(str(year)[:2]) + 1)
  elif year % 100 == 0 and int(str(year)[:2]) != 20:
    return ('{}th century').format(int(str(year)[:2]))
  elif year % 100 >= 1 and year % 100 <= 99 and int(str(year)[:2]) == 20 :
    return ('{}st century').format(int(str(year)[:2])+1)
  elif year % 100 ==0 and int(str(year)[:2]) == 20 :
    return ('{}th century').format(int(str(year)[:2]))

