
def discount(n, txt):
  if txt=="":return n
  a=txt.split(",")
  for i in range(0,len(a)):
    if "%" in a[i]:a[i]=float(a[i][:-1])/100
  for i in range(0,len(a)):a[i]=float(a[i])
  a=sorted(a)
  for i in range(0,len(a)):
    if a[i]<1:n*=1-a[i]
    else:n-=a[i]
  return round(n,2)

