
def months_interval(dateStart, dateEnd):
  mons = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
  ans = set()
  if dateStart > dateEnd: dateStart, dateEnd = dateEnd, dateStart
  while dateStart <= dateEnd:
    ans.add(dateStart.month)
    dateStart += datetime.timedelta(1)
  return [mons[x-1] for x in sorted(ans)]

