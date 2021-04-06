
def num_ways(n, s):
  lst = []
  for i in range(n+1):
    lst.append(0)
  for i in s :
    lst[i] += 1
  for i in range(n+1) :
    lst[i] += sum(lst[i-j] for j in s if i-j > 0)
  return lst[n]

