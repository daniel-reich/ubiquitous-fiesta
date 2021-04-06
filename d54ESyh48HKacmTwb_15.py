
def gcd_2(a,b):
  if a<b:
    a,b=b,a
  if a%b==0:
    return b
  else:
    return gcd_2(b,a%b)
def gcd(lst):
  g=lst[0]
  for i in range(1,len(lst)):
    g=gcd_2(g,lst[i])
  return g
def main():
  lst=list(map(int,input().split()))
  res=gcd(lst)
  print(res)
  return main()

