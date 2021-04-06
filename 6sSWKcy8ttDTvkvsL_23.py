
def after_n_days(days, n):
  d = {"Monday" : 1, "Tuesday" : 2, "Wednesday" : 3, "Thursday" : 4,
  "Friday" : 5, "Saturday" : 6, "Sunday" : 7
  }
  l = []
  for day in days:
  
    value = d.get(day)
    value += n
    while value > 7:
      value = value - 7
​
    for k, v in d.items():
      if v == value:
        l.append(k)
  return l

