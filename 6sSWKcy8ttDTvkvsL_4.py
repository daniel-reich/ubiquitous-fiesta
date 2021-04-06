
def after_n_days(days, n):
  l = ['Sunday', 'Monday','Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
  return [l[(l.index(x)+n)%7] for x in days]

