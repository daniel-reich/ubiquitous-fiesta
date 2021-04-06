
import re
​
def time_to_eat(current_time):
  matches = re.match('(\d+)\:(\d+)', current_time)
  hours = int(matches.group(1)) + (12 if 'p' in current_time else 0)
  minutes = int(matches.group(2))
​
  for meal_time in [7,12,19,31]:
    if hours < meal_time:
      return [meal_time - hours - (minutes != 0), 0 if minutes == 0 else 60 - minutes]

