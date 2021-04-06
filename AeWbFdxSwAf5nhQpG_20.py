
def persistence(num):
  cnt=0
  if -10<=num<10:
    return 0
  while len(str(num))>1:
    t=[]
    s=1
    while num>0:
      t.append(num%10)
      num=num//10
    for c in t:
      s=s*c
    num=s
    cnt+=1
  return cnt

