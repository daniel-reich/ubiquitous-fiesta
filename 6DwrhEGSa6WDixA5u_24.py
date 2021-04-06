
def is_narcissistic(n):
  d=str(n)
  e=len(d)
  num=n
  sum1=0
  while num>0:
    re=num%10
    sum1=sum1+re**e
    num=num//10
  return n==sum1

