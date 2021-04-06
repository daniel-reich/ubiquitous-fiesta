
def leader(arr):
  return [x for i, x in enumerate(arr) if all(y < x for y in arr[i+1:])]

