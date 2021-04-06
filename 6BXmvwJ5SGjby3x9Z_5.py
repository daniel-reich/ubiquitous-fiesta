
def hours_passed(time1, time2):
  a,b=','.join(i[:-6] if i[-2:]=='AM' else str(eval(i[:-6])+12) for i in (time1,time2)).split(',')
  if time1=='12:00 AM':
    return b+' hours'
  elif a==b:
    return "no time passed"
  else:
    return str(eval(b)-eval(a))+' hours'

