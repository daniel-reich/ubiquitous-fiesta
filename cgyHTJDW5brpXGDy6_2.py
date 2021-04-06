
from datetime import datetime
​
def hour(time):
  return datetime.strptime(time, '%I:%M %p').hour
​
def hours_passed(time1, time2):
  hours = hour(time2) - hour(time1)
  return ('{} hours'.format(hours) if hours else 
    'no time passed')

