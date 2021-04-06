
def repeated(s):
  a=0
  for i in range(2,len(s)):
    n=s[:i]
    if n*(len(s)//i)==s:
      a=a+1
  return a!=0

