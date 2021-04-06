
def max_score(s):
  big = 0
  for i in range(1,len(s)):
    left,right = s[:i].count('0'),s[i:].count('1')
    big = max(big,left+right)
  return big

