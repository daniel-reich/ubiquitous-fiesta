
def simple_pair(lst, n):
  for i in range(len(lst) - 1):
    for j in range(lst.index(lst[i + 1]), len(lst)):
      if lst[i] * lst[j] == n:
        return [lst[i], lst[j]]

