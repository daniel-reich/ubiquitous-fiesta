
monthlength = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def process_date(date):
  return (int(date[0:4]), int(date[5:7]), int(date[8:10]))
def is_next(last, year, month, day): 
   if last[0] == 0:
     return True
   elif (year == last[0] and month == last[1] and day == last[2]+1):
     return True
   elif (year == last[0] and month == last[1] + 1 and day == 1 and last[2] >= monthlength[last[1]-1]):
       return True
   elif (year == last[0] + 1 and month == 1 and day == 1 and  last[1] == 12 and last[2] == 31):
     return True
   else:
     return False 
def current_streak(today, lst):
  if(len(lst) == 0):
      return 0
  last = (0, 0, 0)
  streak = 0
  for entry in lst:
    string = entry['date']
    year, month, day = (process_date(string))
    if (is_next(last, year, month, day)):
      streak += 1
      print(streak)
    else:
      streak = 1;
    last = (year, month, day)
  year, month, day = (process_date(today))
  if (is_next(last, year, month, day)):
      return (streak + 1)
  elif (year, month, day) == last: 
      return streak
  else:
      return 0

