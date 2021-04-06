
def is_prime(num):
  a=[]
  for i in range(1,num,1):
    if num%i==0:
      a.append(i)
  if len(a)<2 and num!=1:
    return 1
  else:
    return 0

