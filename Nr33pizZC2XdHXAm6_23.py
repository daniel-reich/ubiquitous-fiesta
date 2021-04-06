
def months_interval(dateStart, dateEnd):
  from datetime import date, timedelta
  s, e = sorted([dateStart, dateEnd])
  vals = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
  ]
  d = dict(enumerate(vals))
  month_indices = sorted(set(
    (s + timedelta(i)).month for i in range((e - s).days + 1)))
  return [d[i - 1] for i in month_indices]

