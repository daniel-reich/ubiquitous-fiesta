
def repeating_cycle(n):
  rest=0
  value=1
  out=[]
​
  for i in range(50000):
    value*= 10
    r=value//n
    value-=r*n
    tmp=[r,value]
    #print(tmp, tmp in out)
    if i>0 and tmp  == out[0]:
      print(out,tmp)
      return ( len(out) -  out.index(tmp) )
    out.append(tmp)
  return -1

