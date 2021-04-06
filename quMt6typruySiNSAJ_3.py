
def shuf(arr):
  return sum(([a,b] for a,b in zip(arr[:len(arr)//2],arr[len(arr)//2:])), [])
​
def shuffle_count(num):
  arr0 = list(range(num))
  curr = arr0.copy()
  cnt = 0
  while True:
    curr = shuf(curr)
    cnt+=1
    if curr == arr0:
      return cnt

