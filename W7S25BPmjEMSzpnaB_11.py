
def bonacci(N,k):
  if k < N:
    return [0 for i in range (k)]
  sequence = [0 for i in range (N-1)]+[1]
  for i in range (k-N):
    sequence.append(sum(sequence[-N:]))
  return sequence[-1]

