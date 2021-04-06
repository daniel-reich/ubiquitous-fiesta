
def remove_repeats(s):
  return ''.join(s[x] for x in range(len(s) - 1) if s[x] != s[x+1]) + s[-1]

