
def is_prime(num):
  a=0
  for i in range (2,8):
    if (num>7 and num%i==0) or (num<7 and num>3 and (num%2==0 or num%3==0)):
      a=+1
    else:
      pass
  if a>0 or num==1:
    return False
  else:
    return True

