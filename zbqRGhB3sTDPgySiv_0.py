
def mod(b,k):
  l=p=1
  if b>k:k,b=b,k
  for i in range(1,b):p*=i;l+=p
  return(0,l)[k>1]

