
def afterNdays(days, n):
  weekdays = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
  return [weekdays[(weekdays.index(day)+n)%7] for day in days]

