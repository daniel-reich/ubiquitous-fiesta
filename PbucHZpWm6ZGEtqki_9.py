
def sliding_sum(lst, n, k):
  position = n - 1
  results = []
  subarray = []
  for item in lst[n - 1:]:
      for x in range(n):
          subarray.insert(0, lst[position - x])
      if sum(subarray) == k:
          results.append(subarray)
      position += 1
      subarray = []
  return results

