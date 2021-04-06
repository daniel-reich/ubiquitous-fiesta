
def bonacci(N, k):
  if (N == 1):
    return 1
    
  window = [0] * N;
  window[N-1] = 1;
  if (k <= N):
    return window[k-1]
    
  counter = 0
  for i in range(0, k-N):
    sum = 0
    for j in range(0,N):
      sum = sum + window[j]
    window[counter] = sum
    if i < k-N-1:
      counter = (counter + 1 ) % N
  return window[counter]

