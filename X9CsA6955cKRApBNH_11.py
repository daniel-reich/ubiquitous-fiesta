
def longest_run(lst):
  r, maxr = 1, 0
  for i in range(len(lst) - 1):
    print(lst[i], lst[i + 1], r)
    if abs(lst[i] - lst[i + 1]) == 1 and not (r > 1 and lst[i + 1] == lst[i - 1]):
      r += 1
    else:
      if r > maxr:
        maxr = r
      r = 1
  return max(maxr, r)

