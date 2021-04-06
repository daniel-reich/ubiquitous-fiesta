
def join_digits(n):
  r=''
  for i in range(1,n+1): r+=str(i)
  return '-'.join(list(r))

