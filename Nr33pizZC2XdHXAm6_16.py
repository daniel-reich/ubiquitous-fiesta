
def months_interval(dateStart, dateEnd):
  months={
  1:"January",
  2:"February",
  3:'March',
  4:'April',
  5:'May',
  6:"June",
  7:'July',
  8:'August',
  9:'September',
  10:'October',
  11:'November',
  12:'December'
  }
  if dateStart>dateEnd:
    [dateStart,dateEnd]=[dateEnd,dateStart]
  if dateStart.year==dateEnd.year:
    monthlist=list(range(dateStart.month,dateEnd.month+1))
  elif dateStart.year==dateEnd.year - 1:
    monthlist=list(range(dateStart.month,13))+list(range(1,dateEnd.month+1))
  else:
    monthlist=list(range(1,13))
  monthsnodupes=[]
  for month in monthlist:
    if month not in monthsnodupes:
      monthsnodupes.append(month)
  monthsnodupes.sort()
  output=[]
  for month in monthsnodupes:
    output.append(months[month])
  return(output)

