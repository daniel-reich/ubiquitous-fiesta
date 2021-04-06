
def bonacci(N, k):
  lst = []
  numberOfZeros = 0
  if (N > 1):
    numberOfZeros = N - 1
  for j in range(numberOfZeros):
    lst.append(0)
  lst.append(1)
  for i in range(k):
    sum = 0
    for l in range(N):
      sum = sum + lst[l + i]
    lst.append(sum)
  return lst[k-1]

