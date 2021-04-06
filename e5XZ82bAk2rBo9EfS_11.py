
def bed_time(*t):
  r=[]
  for i in t:
    alarm = i[0].split(':')
    sleep = i[1].split(':')
    h = int(alarm[0])-int(sleep[0])
    m = int(alarm[1])-int(sleep[1])
    if m<0:
      m+=60
      h-=1
    h=str(h%24)
    m=str(m)
    if len(h)==1: h='0'+h
    if len(m)==1: m='0'+m
    r+=[h+':'+m]
  return r

