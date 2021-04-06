
def format_num(n):
  n=str(n)
  txt=""
  j=1
  for i in n:
    txt+=n[(j*-1)]
    if j%3==0:
      txt+=","
    j+=1
  
  n=""
  j=1
  if txt[-1]==",":
    txt=txt[0:-1]
  for i in txt:
    n+=txt[(j*-1)]
    j+=1
    
  return n

