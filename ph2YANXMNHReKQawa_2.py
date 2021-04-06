
def length_element(r, i):
  ans = []
  total = 0
  for idx, num in enumerate(r):
    total += 1
    if idx == i:
      ans.append(num)
  ans.insert(0, total)
  return ans

