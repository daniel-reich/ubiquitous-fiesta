
def check(arr):
  arr2 = sorted(arr)
  lst = [list(arr2[i:])+list(arr2[:i]) for i in range(len(arr2))]
  return "YES" if arr!=arr2 and any([arr == i for i in lst]) else "NO"

