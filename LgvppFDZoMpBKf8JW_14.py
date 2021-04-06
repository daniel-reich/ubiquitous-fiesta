
def digital_clock(seconds):
  hours = seconds//3600
  min = seconds //60 - (hours*60)
  sec = seconds - ((hours * 60) + min)*60
  if hours >23:
    hours = '00'
  elif hours < 10:
    hours = '0'+str(hours)
  if min < 10:
    min = '0'+str(min)
  if sec < 10:
    print(sec)
    sec = '0'+str(sec)
    print(sec)
  return str(hours)+':'+str(min)+':'+str(sec)

