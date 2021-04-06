
def max_score(s):
  l = len(s)
  cnt = lambda x: s[0:x].count('0') + s[x:l+1].count('1')
  return max([cnt(x) for x in range(1, l)])

