
def discount(n, txt):
  nums=0;percent=[]
  for i in txt.split(', '):
    if '%' in i:percent+=[float(i[:-1])]
    elif i!='':nums+=float(i)
  percent.sort()
  for i in range(len(percent)):n=n*(100-percent.pop())/100
  return round(n-nums,2)

