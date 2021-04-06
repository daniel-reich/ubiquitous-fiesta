
def easter_date(y):
  a=y%19
  b=y>>2
  c=b//25+1
  d=(c*3)>>2
  e=((a*19)-((c*8+5)//25)+d+15)%30
  e+=(29578-a-e*32)>>10
  e-=((y%7)+b-d+e+2)%7
  d=e>>5
  day=e-d*31
  month=d+3
  if  month==3:
    month="March"+" "+str(day)
    return month
  else:
    month="April"+" "+str(day)
    return month

