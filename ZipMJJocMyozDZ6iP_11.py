
def group(lst, size):
  lenL = len(lst)
  lenR = lenL//size + (lenL%size != 0)
  res = [[] for _ in range(lenR)]
  for i in range(lenL):
    res[i%lenR].append(lst[i])
  return res

