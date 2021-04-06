
def difference_two(lst):
  ans = []
  for i in sorted(lst):
    for j in sorted(lst):
      a = list(sorted([i, j]))
      if a[1] - a[0] == 2 and a not in ans:
        ans.append(a)
  return ans

