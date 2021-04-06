
import datetime
def current_streak(today, lst):
  mem=[[]]
  for a,b in zip([day(i['date']) for i in lst],[day(i['date']) for i in lst][1:]):
    if b-a==datetime.timedelta(days=1):
      mem[-1]+=[a,b] if not a in mem[-1] else [b]
    else:mem[-1]+=[a] if not a in mem[-1] else [];mem+=[[b]]
  if len(lst)==1:mem[-1]+=[day(lst[-1]['date'])]
  mem= [i for i in mem if day(today) in i]+[[]]
  return len(mem[0])
  
def day(y_m_d):
  y,m,d=y_m_d.split('-')
  return datetime.date(int(y),int(m),int(d))

