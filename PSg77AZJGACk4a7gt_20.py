
def meme_sum(a, b):
  m = str(a)
  n = str(b)
  l = abs(len(m)-len(n))
  if len(m)<len(n):
    m1 = l*'0'+ m
    lst1 = [int(i) for i in m1]
    lst2 = [int(i) for i in n]
    return int(''.join([str(i+j) for i,j in zip(lst1,lst2)]))
  else:
    n1 = l*'0'+ n
    lst1 = [int(i) for i in n1]
    lst2 = [int(i) for i in m]
    return int(''.join([str(i+j) for i,j in zip(lst1,lst2)]))

