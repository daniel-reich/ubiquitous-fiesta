
def simple_pair(lst, n):
  for n1 in range(len(lst[:-1])):
    for n2 in range(n1+1,len(lst)):
      if lst[n1]*lst[n2]==n:
        return [lst[n1],lst[n2]]

