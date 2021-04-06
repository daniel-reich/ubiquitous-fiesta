
def cons(lst):
  lst = sorted(lst)
  count = {}
​
  for f in lst:
    count[f] = lst.count(f)
​
  if 2 in count.values():
    return False
  
    
  smallest = lst[0]
  biggest  = lst[0]
  for num in lst:
    if num > biggest:
      biggest = num
    elif num < smallest:
      smallest = num
  l_st = [x for x in range(smallest , biggest+1)]
  print(lst , l_st)
  for index in range(len(l_st)):
    if l_st[index] != lst[index]:
      return False
  return True

