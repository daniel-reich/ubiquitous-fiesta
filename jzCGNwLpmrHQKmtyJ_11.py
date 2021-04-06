
def parity_analysis(num):
  temp=num
  sum=0
  while(temp>0):
    sum+=temp%10
    temp=temp//10
  if (sum%2==0 and num%2==0) or (sum%2!=0 and num%2!=0):
    return True
  return False

