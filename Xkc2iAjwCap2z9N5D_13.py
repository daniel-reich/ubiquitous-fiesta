
import calendar
​
def has_friday_13(month, year):
    
    for week in calendar.monthcalendar(year, month):
        for day in week:
            if day == 13 and day == week[4]:
                return True
    return False

