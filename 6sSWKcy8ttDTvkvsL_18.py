
def after_n_days(days, n):
  day = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
  return [day[(day.index(d)+n)%7] for d in days]

