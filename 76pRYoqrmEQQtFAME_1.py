
def is_astonishing(n):
  s=str(n)
  for i in range(1,len(s)):
    a,b=int(s[:i]),int(s[i:])
    if(b*b+b-a*a+a,a*a+a-b*b+b)[a>b]/2==n:return('AB','BA')[a>b]+'-Astonishing'
  return 0

