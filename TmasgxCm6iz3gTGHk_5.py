
def min_length(lst, n):
  x = 1
  while x < len(lst)+1:
    for i in range(len(lst)-x+1):
      if sum(lst[i:i+x])>n:
        return x
    x+=1
  return -1

