
def junction_or_self(n):
  if n<10: return [n/2] if n%2==0 else "Self";
  lst=[]
  for i in range(10,n+1):
    if i + sum([int(n) for n in str(i)]) == n:
      lst.append(i);
  lst.reverse()
  return lst if len(lst)>0 else "Self"

