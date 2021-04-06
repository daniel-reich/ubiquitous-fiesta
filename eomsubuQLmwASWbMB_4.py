
from datetime import datetime
​
def weekday_dutch(date):
    d, m, y = map(int, date.split())
    days = ['zondag', 'maandag', 'dinsdag', 'woensdag', 'donderdag', 'vrijdag', 'zaterdag']
    return days[int(datetime(y, m, d).strftime('%w'))]

