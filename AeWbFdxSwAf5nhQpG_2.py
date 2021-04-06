
def persistence(num):
  cnt=0
  s=1
  while(1==1):  
    s=1
    if len(str(num))<=1:
      break 
    for x in str(num):
      s*=int(x)
    cnt+=1
    num=s
  return (cnt)

