
def bonacci(N, k):
  bonacci = []
  out = 0
  for i in range(N-1):
    bonacci.append(0)
  bonacci.append(1)
  if(k<=N):
    pass
  else:
    for l in range(k-N):
      for i in range(N):
        out += bonacci[-1 * (i + 1)]
      bonacci.append(out)
      out = 0
  return(bonacci[k - 1])

