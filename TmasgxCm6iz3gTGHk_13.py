
def min_length(lst, n):
  m = -1
  for i in range(1, len(lst) + 1, 1):
    for j in range(len(lst) - i + 1):
      sub = (lst[j:i + j])
      if sum(sub) > n:
        return i
  return m

