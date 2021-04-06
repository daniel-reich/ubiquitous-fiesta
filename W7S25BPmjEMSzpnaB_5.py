
def bonacci(N, k):
  lst = [0]*(N-1) + [1]
  while k > len(lst):
    sum = 0
    for i in range(N):
      sum = sum + lst[-1-i]
    lst.append(sum)
    
  return lst[k-1]

