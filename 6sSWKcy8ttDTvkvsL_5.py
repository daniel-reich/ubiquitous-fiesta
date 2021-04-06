
import calendar
names = list(calendar.day_name)
​
def after_n_days(days, n):
  return [names[(names.index(d) + n) % 7] for d in days]

