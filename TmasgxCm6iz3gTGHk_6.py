
def min_length(lst, n):
  matches = [lst[i:j] for j in range(len(lst) + 1) for i in range(len(lst)) if sum(lst[i:j]) > n]
  if not matches:
    return -1
  return len(sorted(matches, key=lambda x: len(x))[0])

