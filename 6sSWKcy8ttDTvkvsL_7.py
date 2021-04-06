
def after_n_days(days, n):
  x = "Sunday Monday Tuesday Wednesday Thursday Friday Saturday".split()
  return [x[(x.index(i)+n)%7] for i in days]

