
def after_n_days(days, n):
  a = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
  return [a[(a.index(day) + (n % len(a)))%len(a)] for day in days]

