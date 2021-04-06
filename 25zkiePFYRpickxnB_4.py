
def count_boomerangs(lst): #w/o built-in
  new, b = [], []
  while lst != []:
    for x in lst[:3]:
      new += [x]
    b += [new]
    new = []
    lst = lst[1:]
  b, boomerang_count = b[:-2], 0
  for x in b:
    if x[0] == x[-1] and x[0] != x[1]:
      boomerang_count += 1
  return boomerang_count
​
def count_boomerangs(lst):
  return sum(1 for x in [[a, b, c] for a, b, c in zip(lst, lst[1:], lst[2:])] if x[0] == x[-1] and x[0] != x[1])

