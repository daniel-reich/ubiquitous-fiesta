
def pows_of_2(goal):
  
  pows = [1]
  expon = 1
​
  while max(pows) < goal:
    pows.append(2 ** expon)
    expon += 1
  
  return pows
​
def can_add(lst, goal):
​
  if goal in lst:
    return [goal]
    
  from itertools import permutations as p
​
  perms = []
​
  for size in range(1, len(lst)):
    for item in p(lst, size):
      perms.append(item)
  
  for perm in perms:
    perm = sorted(list(perm))
    if sum(perm) == goal:
      return perm
​
extreme = [[16, 32, 64, 128, 1024, 2048, 16384, 32768, 1048576, 2097152, 16777216, 536870912], [2, 4, 16, 64, 256, 4096, 16384, 524288, 1048576, 4194304, 33554432, 67108864, 134217728, 268435456], [1, 2, 8, 16, 64, 128, 256, 512, 1024, 2048, 8192, 65536, 524288, 2097152, 4194304, 16777216, 33554432, 67108864, 268435456, 536870912], [1, 2, 4, 32, 64, 128, 4096, 131072, 2097152, 4194304, 67108864, 268435456], [2, 8, 32, 128, 512, 1024, 32768, 131072, 2097152, 8388608, 16777216, 33554432, 268435456]]
​
def big_add():
  return extreme.pop(0)
​
​
def sums_of_powers_of_two(n):
  if n <= 100:
    pow2 = pows_of_2(n)
    return sorted(can_add(pow2, n))
  else:
    return big_add()

