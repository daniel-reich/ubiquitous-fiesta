
from dateutil.relativedelta import *
def months_interval(dateStart, dateEnd):
  months = {'January':0,'February':1,'March':2,'April':3,'May':4,'June':5,'July':6,'August':7, 'September':8,'October':9,'November':10,'December':11}
  def month_range(date1,date2):
    z = []
    while((date1!=date2)):#| (len(z)<12)
      z = z +[date1.strftime('%B')]
      date1 = date1+ relativedelta(months=+1)
​
    return z + [date2.strftime('%B')]
​
  if(dateStart>dateEnd):
    return sorted(list(set(month_range(dateEnd,dateStart))), key=months.get)
  elif(dateStart==dateEnd):
    return [dateStart.strftime('%B')]
  elif(dateStart<dateEnd):
    return sorted(list(set(month_range(dateStart,dateEnd))), key=months.get)

