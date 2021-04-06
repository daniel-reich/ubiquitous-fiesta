
def remove_repeats(s):
  s = list(s)
  i = 1
  while i < len(s):
    while i < len(s) and s[i] == s[i-1]:
      s.pop(i)
    i += 1
  return ''.join(s)

