
def nearest_element(n, lst):
  x = [abs(i - n) for i in lst]
  y = []
  for i in range(len(x)):
    if x[i] == min(x):
      y.append(lst[i])
    else:
      y.append(-1000)
  return y.index(max(y))

