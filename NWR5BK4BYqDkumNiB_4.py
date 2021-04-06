
def digital_division(n):
  digFacCond=True
  prodNum=1
  sumNum=0
  for c in str(n):
    c=int(c)
    sumNum+=c
    prodNum*=c
    if c and n%c: digFacCond=False
  res=1 if digFacCond else 0
  if not n%sumNum: res+=1
  if prodNum and not n%prodNum: res+=1
  if res==3: return 'Perfect'
  elif not res: return 'Indivisible'
  return res

