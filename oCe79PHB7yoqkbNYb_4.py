
def break_point(num):
  arr = list(map(int, str(num)))
  for i in range(1, len(arr)):
    if sum(arr[:i]) == sum(arr[i:]):
      return True
  return False

