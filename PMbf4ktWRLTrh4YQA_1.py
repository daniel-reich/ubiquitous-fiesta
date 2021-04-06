
def add_n_days_to_a_date(date, days):
  d,m,y = int(date[:2]),int(date[2:4]),int(date[4:])
  for i in range(days):
    leap = y%4==0 and (y%100!=0 or y%400==0)
    if d==31 and m in [1,3,5,7,8,10,12]:
      if m==12:
        d,m,y = 1,1,y+1
      else:
        d,m = 1,m+1
    elif d==30 and m in [4,6,9,11]:
      d,m = 1,m+1
    elif d==28 and m==2 and not leap:
      d,m = 1,3
    elif d==29 and m==2 and leap:
      d,m = 1,3
    else:
      d+=1
  d,m,y = [str(i) for i in [d,m,y]]
  if len(d)==1:
    d='0'+d
  if len(m)==1:
    m='0'+m
  return str(d)+str(m)+str(y)

