
def months_interval(dateStart, dateEnd):
  months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
  if abs(dateStart.year - dateEnd.year)>1: 
    return months
  elif dateStart.year == dateEnd.year:
    return months[min(dateStart.month, dateEnd.month)-1: max(dateStart.month, dateEnd.month)]
  else:
    if dateStart.year < dateEnd.year:
      return sorted(set(months[:dateEnd.month] + months[dateStart.month-1:]), key=lambda x:months.index(x))
    return sorted(set(months[:dateStart.month] + months[dateEnd.month-1:]), key=lambda x:months.index(x))

