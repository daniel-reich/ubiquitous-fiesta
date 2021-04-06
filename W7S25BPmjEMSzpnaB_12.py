
cache = {}
def bonacci(N, k):
  if k <= N-1:
    return 0
  if k == N:
    return 1
  result = 0
  if (N, k) in cache:
    result = cache[(N,k)]
  else:
    for i in range(N):
      result += bonacci(N, k-i-1)
    cache[(N,k)] = result
  return result

