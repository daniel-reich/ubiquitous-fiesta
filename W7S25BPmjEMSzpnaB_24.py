
def bonacci(N, k):
  if N > k:
    return 0
  lst = [0]*k
  lst[N-1] = 1
  for i in range(N,k):
    lst[i] = sum(lst[i-N:i])
  return lst[-1]

