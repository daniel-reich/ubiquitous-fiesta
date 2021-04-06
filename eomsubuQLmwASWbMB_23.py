
import calendar
def weekday_dutch(date):
  return ["maandag","dinsdag","woensdag","donderdag","vrijdag","zaterdag","zondag"][calendar.weekday(*list(map(int,date.split()[::-1])))]

