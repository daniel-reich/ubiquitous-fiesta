
def next_number(num):
  arr = [int(x) for x in str(num)]
  i = len(arr) - 1
  while i > 0 and arr[i - 1] >= arr[i]:
    i -= 1
  if i <= 0:
    return num
  j = len(arr) - 1
  while arr[j] <= arr[i - 1]:
    j -= 1
  arr[i - 1], arr[j] = arr[j], arr[i - 1]
  arr[i:] = arr[len(arr) - 1: i - 1: -1]
  return int(''.join([str(r) for r in arr]))

