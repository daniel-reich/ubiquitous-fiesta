
def shuf(arr):
  return sum(([a,b] for a,b in zip(arr[:len(arr)//2], arr[len(arr)//2:])),[])
​
def shuffle_count(num, curr = None):
  if curr and curr == list(range(num)):
    return 0
  if curr is None:
    curr = list(range(num))
  return 1 + shuffle_count(num, shuf(curr))

