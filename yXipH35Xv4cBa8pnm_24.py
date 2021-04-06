
def microwave_buttons(time):
  c,[m,s]=0,map(int,time.split(":"))
  if not s%30 and m<2 and s<=60:
    c=(m*60+s)//30
  else:
    m,s=map(str,[m,s])
    if m!="0":
      if len(s)==1:
        c=len(m+"0"+s)
      else:
        c=len(m+s)
    elif m=="0" and s!="0":
      c=len(s)
  return c+1

