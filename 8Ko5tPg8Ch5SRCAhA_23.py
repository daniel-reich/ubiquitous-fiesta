
def fibonacci(num):
  lst = [1, 1]
  if num < 2:
    return 1
  for i in range(2, num + 1):
    lst.append(lst[i - 2] + lst[i - 1])
  return lst[num]

