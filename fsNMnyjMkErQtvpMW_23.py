
def holey_sort(lst):
  return sorted(lst, key=sortedd)
  
  
def sortedd(n):
  n = str(n)
  x = 0
  ones = "0469"
  twos = "8"
  for i in n:
    if i in ones:
      x+=1
    elif i in twos:
      x+=2
  return x

