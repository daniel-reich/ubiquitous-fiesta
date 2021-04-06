
def num_ways(n, s):
  d = {}
  def helper(n, s):
    if n < 0:
      return 0
    if n <= 1:
      return 1
    if n not in d:
      d[n] = sum([helper(n-i,s) for i in s])
    return d[n]
  helper(n, s)
  return d[n]

