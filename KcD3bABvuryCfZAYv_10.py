
def most_frequent_char(lst):
  x = ''.join(lst)
  y = [x.count(i) for i in x]
  z = []
  for i in range(len(x)):
    if max(y) == y[i]:
      z.append(x[i])
  return sorted(list(set(z)))

