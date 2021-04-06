
def count_repetitions(lst):
  counts = {}
  for i in lst:
    if i not in counts:
      counts[i] = 1
    else:
      counts[i] += 1
  return counts

