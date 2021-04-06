
import calendar
​
def weekday_dutch(date):
  day, month, year = (int(i) for i in date.split(' '))     
  dayNumber = calendar.weekday(year, month, day) 
  days =["maandag", "dinsdag", "woensdag", "donderdag", 
                         "vrijdag", "zaterdag", "zondag"] 
  return (days[dayNumber])

