
def is_positive_dominant(lst):#w/o built-in
  p, n = [], []
  for x in lst:
    if x > 0:
      if x not in p:
        p += [x]
    elif x < 0:
      if x not in n:
        n += [x]
  l_p, l_n = 0, 0
  while p != []:
    l_p += 1
    p = p[1:]
  while n != []:
    l_n += 1
    n = n[1:]
  return l_p > l_n
​
def is_positive_dominant(lst):
  return len(set(i for i in lst if i > 0)) > len(set(i for i in lst if i < 0))

