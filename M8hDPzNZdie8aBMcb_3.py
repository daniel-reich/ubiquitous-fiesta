
def count_substring(s, r=0):
  for n, ch in enumerate(s):
    if ch == 'A':
      r += s[n:].count('X')
  return r

