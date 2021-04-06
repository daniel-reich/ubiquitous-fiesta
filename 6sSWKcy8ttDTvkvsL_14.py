
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 
        'Friday', 'Saturday', 'Sunday']
​
def after_n_days(days, n):
  days = [weekdays.index(d) for d in days]
  return [weekdays[(di + n) % 7] for di in days]

