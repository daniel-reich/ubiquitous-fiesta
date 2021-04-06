
def sync_subs(subtitles, timeIncrement):
  if problem(timeIncrement): return 'There is a problem with the second argument'
  subtitles = subtitles.split('\n')
  for i in range(len(subtitles)):
    if '-->' in subtitles[i]:
      subtitles[i] = fixtime(timeIncrement,subtitles[i])
  return '\n'.join(subtitles)
​
def fixtime(inc, time):
  inc = inc.split(':')
  inc = inc[:-1]+inc[-1].split(',')
  time = time.split(' --> ')
  for i in range(len(time)):
    temp = time[i].split(':')
    temp = temp[:-1]+temp[-1].split(',')
    for x in range(len(temp)):
      temp[x] = int(temp[x])+int(inc[x])
    if temp[3] >= 1000:
      temp[2] += temp[3]//1000
      temp[3] = temp[3]%1000
    if temp[2] >=60:
      temp[1] += temp[2]//60
      temp[2] = temp[2]%60
    if temp[1] >= 60:
      temp[0] += temp[1]//60
      temp[1] = temp[1]%60
    temp = [str(i) for i in temp]
    for x in range(3):
      if len(temp[x]) < 2:
        if len(temp[x]) ==1: temp[x] = '0'+temp[x]
    if len(temp[3])<3:
      if len(temp[3])==1: temp[3] = '00'+temp[3]
      else: temp[3] = '0' + temp[3]
    temp = temp[0]+':'+temp[1]+':'+temp[2]+','+temp[3]
    time[i] = temp
  return ' --> '.join(time)
  
def problem(inc):
  if inc.count(':') != 2 or inc.count(',') != 1: return True
  inc = inc.split(':')
  inc = inc[:-1] + inc[-1].split(',')
  for i in range(3):
    if int(inc[i])>=60: return True
  if int(inc[-1])>=1000: return True
  return False

