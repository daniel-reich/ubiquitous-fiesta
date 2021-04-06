
def months_interval(dateStart, dateEnd):
  if dateStart - dateEnd > datetime.timedelta(0):
    a1 = dateEnd
    a2 = dateStart
  else:
    a1 = dateStart
    a2 = dateEnd
  m =['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
  i = a1.month
  lst = {i-1:m[i-1]}
  while a1.month != a2.month or a1.year != a2.year:
    i += 1
    if i > 12:
      i = i - 12
      a1 = datetime.date(a1.year +1 , i , 1)
    a1 = datetime.date(a1.year , i , 1)
    if not m[i-1] in lst:
      lst.update({i-1:m[i-1]})
  return [lst[i] for i in sorted(lst.keys())]

