
def months_interval(dateStart, dateEnd):
  months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
  [d1,d2]=sorted([dateStart,dateEnd])
  span = d2.month-d1.month+12*(d2.year-d1.year)
  return sorted(set([months[i%12] for i in range(d1.month-1,d1.month+span)]),key=lambda x:months.index(x))

