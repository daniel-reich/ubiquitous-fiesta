
def make_transpose(m):
  ans = []
  for i in range(len(m[0])):
    ans += [i*[]]
  for i in range(len(m[0])):
    for j in range(len(m)):
      ans[i] += [m[j][i]]
  return ans

