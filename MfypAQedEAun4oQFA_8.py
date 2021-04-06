
def perrin(n):
  lst = [3, 0, 2]
  count = 3
  while count <= n:
    lst.append(lst[count - 2] + lst[count - 3])
    count += 1
  return lst[n]

