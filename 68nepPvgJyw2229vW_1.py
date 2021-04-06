
def pairwise_swap(lst):
  for i in range(0,len(lst)-1,2):
    lst[i:i+2] = lst[i:i+2][::-1]
  if len(lst)%2:
    i = max(range(len(lst)), key = lambda i: value(lst[i]))
    lst[i], lst[len(lst)-1] = lst[len(lst)-1], lst[i]
  return lst
  
​
value = lambda n: sum(ord(s) for s in str(n))

