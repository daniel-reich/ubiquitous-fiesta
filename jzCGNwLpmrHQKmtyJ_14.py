
def parity_analysis(num):
  b=str(abs(num))
  a=len(b)
  sum1=0
  for i in range(0,a):
    sum1=sum1+int(b[i])
  if((sum1%2==0 and num%2==0) or (sum1%2!=0 and num%2!=0)):
    return True
  else:
    return False

