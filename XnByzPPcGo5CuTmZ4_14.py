
def kix_code(n):
  n=n.split(",")
  a=n[2]
  while(a[0]==" "):
    a=a[1:]
  
  a=a.split(" ")
  a=a[0]+a[1]
  b=''
  for i in range(0,len(n[1])):
    if(n[1][i]>='0' and n[1][i]<='9'):
      b=n[1][i:]
      break
  b=b.upper()
  b=b.replace(" ","X")
  b=b.replace("-","X")
  b=b.replace("/","X")
  return a+b

