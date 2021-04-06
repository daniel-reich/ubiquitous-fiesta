
def holey_sort(lst):
  d = {
    1: 0,
    2: 0,
    3: 0,
    4: 1,
    5: 0,
    6: 1,
    7 : 0,
    8 : 2,
    9: 1,
    0: 1
  }
  arr, brr = [], []
  for x in lst:
    k = 0
    for c in str(x):
      k += d[int(c)]
    arr.append([k,x])
​
  for i in range(min(arr)[0],max(arr)[0]+1):
    for q in arr:
      if q[0] == i:
        brr.append(q[1])
  return brr

