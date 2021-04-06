
import calendar
​
def weekday_dutch(date):
    days = ['maandag', 'dinsdag', 'woensdag', 'donderdag', 'vrijdag', 'zaterdag', 'zondag']
    date_split = [int(i) for i in date.split(' ')]
    y, m, d = date_split[2], date_split[1], date_split[0]
    return days[calendar.weekday(y, m, d)]

