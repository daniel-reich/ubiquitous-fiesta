
def after_n_days(days, n):
  day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'] 
  return [day[(day.index(i) + n) % len(day)] for i in days]

