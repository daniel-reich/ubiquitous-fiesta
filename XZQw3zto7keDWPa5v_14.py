
def day_amount(month, year):
  dateDict = {1:31,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
  if month in dateDict:
    return dateDict[month]
  elif (year % 400 == 0) and (year % 100 == 0):
    return 29
  elif year % 4 == 0:
    if year % 100 != 0:
      return 29
    else:
      return 28
  else:
    return 28

