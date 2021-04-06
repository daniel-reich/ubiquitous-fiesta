
from datetime import datetime, timedelta
​
def time_difference(city_a, timestamp, city_b):
    d = {
        'Los Angeles': '-08:00'.split(':'),
        'New York': '-05:00'.split(':'),
        'Caracas': '-04:-30'.split(':'),
        'Buenos Aires': '-03:00'.split(':'),
        'London': '00:00'.split(':'),
        'Rome': '01:00'.split(':'),
        'Moscow': '03:00'.split(':'),
        'Tehran': '03:30'.split(':'),
        'New Delhi': '05:30'.split(':'),
        'Beijing': '08:00'.split(':'),
        'Canberra': '10:00'.split(':')
    }
​
    a = datetime.strptime(timestamp, '%B %d, %Y %H:%M')
    a -= timedelta(hours=int(d[city_a][0]), minutes=int(d[city_a][1]))
    a += timedelta(hours=int(d[city_b][0]), minutes=int(d[city_b][1]))
​
    return a.strftime('%Y-%-m-%-d %H:%M')

