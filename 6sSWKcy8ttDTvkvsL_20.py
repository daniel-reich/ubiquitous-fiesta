
def after_n_days(days, n):
  week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 
          'Friday', 'Saturday', 'Sunday')
  return [week[(week.index(day) + n) % 7] for day in days]

