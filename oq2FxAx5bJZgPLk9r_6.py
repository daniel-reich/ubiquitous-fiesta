
def sock_merchant(lst):
  colors = {}
  for i in lst:
    if i not in colors:
      colors[i] = 1
    else:
      colors[i] += 1
  counts = [colors[i]//2 for i in colors]
  return sum(counts)

