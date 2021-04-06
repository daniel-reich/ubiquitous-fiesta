
def return_unique(lst):
  l = []
  for i in range(len(lst)):
    print("hello")
    print(lst.count(lst[i]) == 1)
    if lst.count(lst[i]) == 1:
      l += [lst[i]] 
  return l

