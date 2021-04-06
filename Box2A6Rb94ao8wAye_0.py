
def leader(arr):
  return [arr[i] for i in range(len(arr)) if max(arr[i:])==arr[i]]

