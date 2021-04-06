
def gcd(a, b):
  while b:
    a, b = b, a % b
  return a
  
def ecg_seq_index(n):
  nums, last, idx = set([1,2]), 2, 1
  while last != n:
    cur = 1
    while cur in nums or gcd(cur, last) == 1:
      cur += 1
    nums.add(cur)
    last = cur
    idx += 1
  return idx

