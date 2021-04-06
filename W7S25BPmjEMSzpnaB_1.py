
def bonacci(N, k):
  f = [0]*(N-1)+[1]
  for i in range(k-1):
    f.append(sum(f[-N:]))
  return f[k-1]

