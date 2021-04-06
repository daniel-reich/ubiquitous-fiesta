
def zipper(a, b):
  return sum([int(x + y) for x, y in zip(a, b)])
​
def closing_in_sum(num):
  n = str(num)
  l = len(n)
  a = n[:l//2] 
  b = n[l//2 + 1:] if l % 2 else n[l//2:]
  c = n[l//2]
  return zipper(a, b) + int(c) if l % 2 else zipper(a, b)

