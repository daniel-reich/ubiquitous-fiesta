
def after_n_days(days, n):
  d = {
    "Sunday":0,
    "Monday":1,
    "Tuesday":2,
    "Wednesday":3,
    "Thursday":4,
    "Friday":5,
    "Saturday":6
  }
​
​
  arr = [(d[day] + n)%(len(d))for day in days]
  l = []
  for n in arr:
    l.append([k for k,v in d.items() if v == n])
  return sum(l,[])

