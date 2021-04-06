
def group_seats(lst, n):
  w = '0' * n
  ans = 0
  for k in lst:
    s = ''.join([str(v) for v in k]) 
    if w in s:
      for wi in range(len(s)):
        ans = ans + (s[wi:wi+n] == w)
  return ans

