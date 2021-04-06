
def is_economical(n):
  x,y,i=len(str(n)),0,2
  while n!=1:
    c=0
    while not n%i:c+=1;n//=i
    if c:y+=len((str(i))+(str(c) if c>1 else ''))
    i+=1
  return 'Equidigital' if x==y else 'Frugal' if x>y else 'Wasteful'

