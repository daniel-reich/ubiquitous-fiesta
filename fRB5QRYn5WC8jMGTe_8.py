
from datetime import datetime, timedelta
​
def time_difference(city_a, timestamp, city_b):
    offset_hours = {'Los Angeles': -8, 'New York': -5, 'Caracas': -4.5, 'Buenos Aires': -3, 'London': 0,
                        'Rome': 1, 'Moscow': 3, 'Tehran': 3.5, 'New Delhi': 5.5, 'Beijing': 8, 'Canberra': 10}
    dt_a = datetime.strptime(timestamp,'%B %d, %Y %H:%M')
    delta_hours = offset_hours[city_b] - offset_hours[city_a]
    dt_b = dt_a + timedelta(hours=delta_hours)
    # Are f-strings not supported in edabit's version of Python?
    return '{}-{}-{} {:02}:{:02}'.format(dt_b.year,dt_b.month,dt_b.day,dt_b.hour,dt_b.minute)

