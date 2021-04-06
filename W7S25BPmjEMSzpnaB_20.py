
def bonacci(N, K):
  if N == 1:
    return 1
  else:
    list_out = []
    for _ in range(N - 1):
      list_out.append(0)
    list_out.append(1)
    for i in range(N, K):
      list_out.append(sum(list_out[-1:-1 - 1 * N:-1]))
    return list_out[K - 1]

