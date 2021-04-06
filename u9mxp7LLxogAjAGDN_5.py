
def factor(num):
  s = 0
  for i in range(1, num + 1):
    if num % i == 0:
      s += 1
  return s
​
def factor_sort(nums):
  d = {}
  for i in nums:
    d[i] = factor(i)
  d = (sorted(d.items(), key=lambda x: (x[1], x[0]), reverse=True))
  return [i[0] for i in d]

