
def afterNdays(days, n):
  weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday',
  'Saturday','Sunday']
​
  return [weekdays[(weekdays.index(day) + n) % 7] for day in days]

