
def zero_indices(lst, k):
  zero_pos = [-1] + [p for p in range(len(lst)) if lst[p]==0] + [len(lst)]
  z = len(zero_pos)
  i = sorted(list(range(z-k-1)),key = lambda i: (zero_pos[i+k+1]-zero_pos[i],-i))[-1]
  return zero_pos[i+1:i+k+1]

