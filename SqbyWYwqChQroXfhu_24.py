
def lower_triang(arr):
  return [row[:i] + [0]*(len(row)-i) for i, row in enumerate(arr, 1)]

