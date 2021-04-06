
def who_goes_free(n, k):
  i = 0
  lst = []
  while(i < n):
    lst.append(i)
    i = i + 1
  i = k - 1
  while(len(lst) > 1):
    del(lst[i])
​
    i = i + k - 1
    while(i > len(lst)):
      i = i - len(lst)
    if(i == len(lst)):
      i = 0
  return lst[0]

