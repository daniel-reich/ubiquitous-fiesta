
def perrin(n):
  lst = [3, 0, 2]
  if n < 3:
    return lst[n]
  for i in range(n - 1):
    lst.append(lst[i] + lst[i + 1])
  return lst[n]

