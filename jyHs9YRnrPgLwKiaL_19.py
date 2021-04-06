
def split(x):
  max=0;i=0;a=1
  while(a>max):
    max=a
    i=i+1
    a=(x/i)**i
  return (round(max,1))

