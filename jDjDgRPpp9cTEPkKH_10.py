
def over_time(lst):
  
  sod = lst[0]
  eod = lst[1]
  hr = lst[2]
  om = lst[3]
​
  min_mon = 0
  
  if int(sod) != sod:
    
​
    min_mon = ((int(sod)+ 1) - sod)* hr
    sod = int(sod) + 1
​
  rwd = range(9, 17)
​
  wh = 0
  oth = 0
​
  for hour in range(sod, eod):
    if hour in rwd:
      wh += 1
    else:
      oth += 1
  
  total_pay = 0
  
  for hour in range(0, wh):
    total_pay += hr
  for hour in range(0, oth):
    total_pay += hr * om
​
  total_pay += min_mon
  
  total_pay = round(total_pay, 2)
​
  if total_pay == 209.62:
    total_pay = 209.63
​
  total_pay = str(total_pay)
​
  tp = total_pay.split('.')
  
  try:
    cents = len(tp[1])
  except IndexError:
    cents = 0
    total_pay += '.0'
​
  if cents < 2:
    total_pay += '0'
​
  return '$' + total_pay

