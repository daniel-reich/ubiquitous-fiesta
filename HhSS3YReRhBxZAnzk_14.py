
def gen_values(n, i):
  j = 0.0
  ans = []
  while round(j, 2) <= n:
    ans.append(round(j, 2))
    j += i
  return ans

