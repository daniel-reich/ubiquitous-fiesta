
import datetime
​
def days_until_2021(date):
  
  Blocks = date.split("/")
  
  Current_Day = int(Blocks[1])
  Current_Month = int(Blocks[0])
  Current_Year = int(Blocks[2])
  
  Current_Date = datetime.datetime(Current_Year, Current_Month, Current_Day)
  Target_Date = datetime.datetime(2021, 1, 1)
  
  Duration = Target_Date - Current_Date
  Duration = Duration.days
  
  if (Duration == 1):
    Answer = str(Duration) + " day"
    return Answer
  else:
    Answer = str(Duration) + " days"
    return Answer

