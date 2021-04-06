
def max_score(s):
  A=[(s[:i].count('0'), s[i:].count('1')) for i in range(1, len(s))]
  return max(sum(x) for x in A)

