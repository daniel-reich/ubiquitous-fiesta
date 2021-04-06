
def number_pairs(txt):
  arr = txt.split()[1:]
  k = 0
  for x in set(arr):
    y = arr.count(x)
    while y > 1:
      k += 1
      y -= 2
  return k

