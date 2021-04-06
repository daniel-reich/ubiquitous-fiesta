
import re
def sync_subs(subtitles, timeIncrement):
  #handle incorrect timeIncrement
  y=timeIncrement.split(':')
  if (len(y)==3):
    if len(y[0])!=2 or len(y[1])!=2 or len(y[2])!=6 or int (y[0])>=60\
    or int (y[1])>=60 or ',' not in y[2]:
      return('There is a problem with the second argument')
  else:
    return('There is a problem with the second argument')
​
  subtitles1=subtitles
  strings,overflow=re.findall('[\w\W\s\S\d\D](\d{2}:\d{2}:\d{2},\d{3})[\w\W\s\S\d\D]',subtitles),0
  for i in range(len(strings)):
    first = strings[i]
    fraction,overflow = (int(first.split(',')[-1])+ int(timeIncrement.split(',')[-1])),0
    if(fraction >=1000):
      fraction,overflow  = fraction-1000,1
    fraction=str(fraction)
    while not  (len(fraction)==3):
      fraction = '0'+fraction
    
    seconds = overflow+ int(first.split(',')[0].split(':')[-1]) + int(timeIncrement.split(',')[0].split(':')[-1])
    if seconds >=60:
      seconds, overflow = seconds-60,1
    else:
      overflow=0
    seconds=str(seconds)
    if len(seconds)==1:
      seconds = '0'+seconds
    
    minutes = overflow+ int(first.split(',')[0].split(':')[1]) + int(timeIncrement.split(',')[0].split(':')[1])
    if minutes >=60:
      minutes, overflow = minutes-60,1
    else:
      overflow=0
    minutes=str(minutes)
    if len(minutes)==1:
      minutes = '0'+minutes
    
    hours = overflow+ int(first.split(',')[0].split(':')[0]) + int(timeIncrement.split(',')[0].split(':')[0])
    if hours >=23:
      hours=hours%24
    hours=str(hours)
    if len(hours)==1:
      hours = '0'+hours
    subtitles1=subtitles1.replace(first,hours+':'+minutes+':'+seconds+','+fraction)
  return subtitles1

