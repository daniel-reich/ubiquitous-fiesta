
def min_length(lst, n):
  for i in range(1, len(lst) + 1):
    v = [lst[j:j + i] for j in range(0, len(lst) - i + 1)]
    for k in v:
      if sum(k) > n:
        return i
  return -1

