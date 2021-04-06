
def check(lst):
  arr = sorted(lst)
  for i in range(len(lst)):
    arr.append(arr[0])
    arr.pop(0)
    if lst == arr and arr != sorted(lst):
      return "YES"
  return "NO"

