
def time_adjust(now, h, m, s):
  y=""
  y2=""
  y3=""
  x = sum([h*3600, m*60, s])+([int(x) for x in now.split(":")][0]*3600) + ([int(x) for x in now.split(":")][1]*60)+([int(x) for x in now.split(":")][2])
  while x>=86400:
    x-= 86400
  if (x//3600) < 10:
    y="0"
  if (x%3600)//60 < 10:
    y2="0"
  if (x%3600)%60 < 10:
    y3="0"
  return "".join([y, str(x//3600), ":" , y2,str((x%3600)//60) , ":" ,y3, str((x%3600)%60)])

