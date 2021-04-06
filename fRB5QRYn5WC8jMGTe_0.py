
from datetime import datetime as dt, timedelta
​
def time_difference(city_a, timestamp, city_b):
    d = {'Los Angeles': -8, 'New York': -5, 'Caracas': -4.5, 
         'Buenos Aires': -3, 'London': 0, 'Rome': 1, 
         'Moscow': 3, 'Tehran': 3.5, 'New Delhi': 5.5, 
         'Beijing': 8, 'Canberra': 10}
​
    time_difference = d[city_b] - d[city_a]
    time_current = dt.strptime(timestamp, '%B %d, %Y %H:%M')
    time_new = time_current + timedelta(hours=time_difference)
    
    return time_new.strftime('%Y-%-m-%-d %H:%M')

