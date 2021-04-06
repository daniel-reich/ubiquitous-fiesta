
def make_dartboard(n):
  if n%2==1:
    lst = ['1'*n]*(n//2+1)
    for i in range(1,n//2+1):
      lst[i]=lst[i-1][:i]+(str(i+1)*(n-(2*i)))+lst[i-1][-i:]
    lst+=lst[:-1][::-1]
  else:
    lst = ['1'*n]*(n//2)
    for i in range(1,n//2):
      lst[i]=lst[i-1][:i]+(str(i+1)*(n-(2*i)))+lst[i-1][-i:]
    lst+=lst[::-1]
  return [int(i) for i in lst]

