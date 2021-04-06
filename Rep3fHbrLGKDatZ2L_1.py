
def complete_pattern(s):
  for l in range(len(s)//2, 0, -1):
    if all([s[i] == s[i+l] or s[i] == '_' or s[i+l] == '_' for i in range(l)]):
      i = s.find('_')
      return s[:l][i % l] if i >= l else s[l:][i % l]

