
def shuffle_count(n):
  c = 0
  lst = [x for x in range(1, n+1)]
  lst1 = [a for a in lst]
  while True:
    k = []
    c += 1
    for a, b in zip(lst[:(n//2)+1], lst[(n//2):]):
      k.append(a)
      k.append(b)
    if k == lst1:
      return c
    lst = [a for a in k]

