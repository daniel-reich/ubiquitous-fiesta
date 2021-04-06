
import datetime
def weekday_dutch(date):
  arr = ["maandag","dinsdag","woensdag","donderdag","vrijdag","zaterdag","zondag"]  
  index = datetime.datetime.strptime(date, '%d %m %Y').weekday() 
  return arr[index]

