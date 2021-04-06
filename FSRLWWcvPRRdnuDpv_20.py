
from datetime import datetime as dt
​
def time_to_eat(current_time):
  meal_times = [dt.strptime(i, '%H:%M') for i in ('07:00', '12:00', '19:00')]
  t = dt.strptime(current_time.replace('.', '').upper(), '%I:%M %p')
  nearest = min((m - t).seconds for m in meal_times)
  
  return [nearest//3600, nearest%3600//60]

