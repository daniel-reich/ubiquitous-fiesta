
def is_valid_subsequence(l, s):
  if s and s[0] in l:
    return is_valid_subsequence(l[l.index(s[0]) + 1:], s[1:])
  return not s

