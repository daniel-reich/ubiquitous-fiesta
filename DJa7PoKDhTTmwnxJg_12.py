
def adjacent_product(lst):
  adj = []
  for i in range(0,len(lst)-1):
    adj.append(lst[i] * lst[i+1])
  return max(adj)

