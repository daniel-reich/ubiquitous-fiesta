
def bonacci(n, k):                    # N-bonacci numbers
  """ Return the k-th term of the n-bonacci sequence """
  if n==1: return 1
  arr = [0]*(n-1) + [1]
  [arr.append(sum(arr[i:i+n])) for i in range(k-n)]
  return arr[k-1]

