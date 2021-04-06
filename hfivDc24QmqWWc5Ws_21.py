
def eratosthenes(num):
  ans = []
  for i in range(2, num + 1):
    for j in range(2, i):
      if i % j == 0:
        break
    else:
      ans.append(i)
  return ans

