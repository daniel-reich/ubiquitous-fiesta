
def microwave_buttons(time):
  ts = [ int(i) for i in time.split(":") ]
  totalsec = ts[0]*60 + ts[1]
  if totalsec == 0 : 
    return 1
  if totalsec <= 60 and ts[1] <= 60 : 
    t1 = totalsec // 30 + 1 if totalsec >= 30 else len(str(totalsec)) + 1 
    t2 = len(str(totalsec)) + 1 
  else : 
    return len(time.strip(':').lstrip('0')) 
  return t1 if t1<t2 else t2

