
def day_of_year(date):
  datelist = date.split('/')
  daylist = []
  totaldays = 0
  year = int(datelist[2])
  if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    daylist = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  else:
    daylist = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
  for i in range(int(datelist[0]) - 1):
    totaldays += daylist[i]
  totaldays += int(datelist[1])
  return totaldays

