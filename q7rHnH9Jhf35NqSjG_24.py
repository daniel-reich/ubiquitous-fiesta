
def trailing_zeros(n):
  c,lst,p=0,[],1
  while 5**p<n:
    lst.append(p)
    p+=1
  for x in lst:
    c+=n//(5**x)
  return c

