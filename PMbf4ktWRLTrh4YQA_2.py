
def add_n_days_to_a_date(date, days):
  months = {1:31,2:(28,29),3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
  day,month,year=int(date[0:2]),int(date[2:4]),int(date[4:])
  days1=days
  yearsToCurrent=days1//365
  if month>2 or month==2 and day==29:
    st=1
  else:
    st=0
  leapExtra=0
  for i in range(year+st,year+yearsToCurrent+1):
    isLeap = (i%4==0) if (i%100!=0) else (i%400==0)
    if(isLeap):
      if (month>2 or month==2 and day==29):
        leapExtra+=1
  year=year+yearsToCurrent
  days1-=(365*yearsToCurrent+leapExtra)
  while days1>0:
    for key, value in months.items():
      if key == month:
        isLeap = (year%4==0) if (year%100!=0) else (year%400==0)
        
        if month==2:
          if (isLeap):
            month_days=months[key][1]
          else:
            month_days=months[key][0] 
        else:
          month_days=months[key]
        
        if(days1-(month_days-day))>0:
          days1-=(month_days-day)
          day=0
          if(month+1)>12:
            month=1
            year+=1
            isLeap = (year%4==0) if (year%100!=0) else (year%400==0)
          else:
            month=month+1
        else:
          day= day+days1
          days1=0
          break
  d='0'+str(day) if day<10 else str(day)
  m='0'+str(month) if month<10 else str(month)
  return(d+m+str(year))

