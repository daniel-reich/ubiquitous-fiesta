
def mystery_func(num):
  temp=num
  rev=1
  while(temp!=0):
   fact=temp%10
   rev=fact*rev
   temp=int(temp/10)
  return(rev)

