
def add_bill(money):
  k=1000
  f=0
  v=""
  l=money.split(",")
  ml=[i for i in l if i[0] =="d"]
  for i in ml:
    if "k" in i:
      v=str(int(i[1:-1])*k)
      ml[ml.index(i)]=i[0]+v
  for i in ml:
    f+=int(i[1:])
  return f

