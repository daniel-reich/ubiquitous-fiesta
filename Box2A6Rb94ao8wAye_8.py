
def leader(arr):
  return [arr[i] for i in range(len(arr)) if arr[i]==max(arr[i:])]

