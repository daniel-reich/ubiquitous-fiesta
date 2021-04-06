
def square_digits(n):
  temp=n
  s=''
  sq=0
  while temp>0:
    dig=temp%10
    sq=dig**2
    temp=temp//10
    s=str(sq)+s
  return int(s)

