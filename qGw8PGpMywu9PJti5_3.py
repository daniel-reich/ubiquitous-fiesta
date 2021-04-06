
def hanoi(n):
  if n==0:
    return []
  elif n==1:
    return [(1,3)]
  else:
    l1 = [tuple((tup[i] - 1)*2 % 3 + 1 for i in [0,1]) for tup in hanoi(n-1)]
    l2 = [(1,3)]
    l3 = [tuple((tup[i] + 1)*2 % 3 + 1 for i in [0,1]) for tup in hanoi(n-1)]
    return l1 + l2 + l3

