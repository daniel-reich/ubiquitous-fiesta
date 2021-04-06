
def bonacci(N, k):
  if k < N:
    return 0
  lst = [0]*(N-1) + [1]
  for i in range(k-N):
    lst.append(sum(lst[-N:]))
  return lst[-1]

