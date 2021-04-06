
def lower_triang(arr):
  return [arr[x-1][:x] + [0] * (len(arr[0])-x) for x in range(1, len(arr)+1)]

