
def stock_picker(lst):
  best, curr = [10**4, -1], [10**4, -1]
  for i in range(len(lst)-1):
    if lst[i] < curr[0]:
      curr = [lst[i], -1]
    if lst[i+1] - curr[0] > curr[1]:
      curr[1] = lst[i+1] - curr[0]
    if curr[1] > best[1]:
      best = curr[::]
  return best[1]

