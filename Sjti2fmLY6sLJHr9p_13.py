
def look_and_say(start, n):
  sezman3=[start]
  for e in range(n-1):
    start=str(start)
    seznam=[]
    i=1
    x=start[0]
    while i<len(start):
      if start[i]==start[i-1]:
        x+=start[i]
        i+=1
      else:
        seznam.append(x)
        x=start[i]
        i+=1
    seznam.append(x)
    seznam2=[]
    for k in seznam:
      seznam2.append(str(len(k))+k[0])
    sezman3.append(int("".join(seznam2)))
    start=sezman3[-1]
  return(sezman3)

