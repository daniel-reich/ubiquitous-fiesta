
def entry(r,c):
  return min(r,c) + 1 
def convert(lst):
  string = [str(el) for el in lst]
  return ''.join(string)
def make_dartboard(n):
  lst = [[entry(i,j) for j in range(0,n//2)] for i in range(0,n//2)]
  for i in range(0,len(lst)):
    lst[i].extend(lst[i][::-1])
    if n % 2 == 1:
      lst[i].insert(n//2,i+1)
  lst.extend(lst[::-1])
  if n % 2 == 1:
    lst.insert(n//2,list(range(1,n//2 + 1)))
    lst[n//2].extend(list(range(1,n//2 + 1))[::-1])
    lst[n//2].insert(n//2,n//2 + 1)
  return list(map(lambda x: int(convert(x)),lst))

