
def after_n_days(days, n):
  lst = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  n = n % 7
  for k in range(0, len(days)):
    pos = lst.index(days[k])
    pos += n
    newpos = pos % 7
    days[k] = lst[newpos]
  return days

