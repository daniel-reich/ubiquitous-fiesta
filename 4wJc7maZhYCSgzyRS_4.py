
def two_product(arr, N):
  seen = {}
  for i in range(len(arr)):
    if arr[i] in seen:
      return [seen[arr[i]], arr[i]]
    f, r = divmod(N, arr[i])
    if r == 0 and not f in seen:
      seen[f] = arr[i]
  return None

